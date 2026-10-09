from pathlib import Path
import json
import re
import numpy as np
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from .risk_engine import robust_anomaly, trend_score, vaccination_gap, climate_signal, risk_score, risk_tier, explain, surveillance_freshness

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "processed"
OUT.mkdir(parents=True, exist_ok=True)

AFRO_COUNTRIES = set(pd.read_csv(ROOT / "config" / "countries.csv")["country"])

def read_owid(name):
    p = RAW / f"{name}.csv"
    if not p.exists():
        raise FileNotFoundError(f"{p} missing. Run: python scripts/download_data.py")
    df = pd.read_csv(p)
    # OWID standard columns are Entity, Code, Year, plus one value column.
    value = [c for c in df.columns if c not in {"Entity", "Code", "Year"}][0]
    return df.rename(columns={"Entity":"country", "Code":"iso3", "Year":"year", value:"value"})[
        ["country","iso3","year","value"]
    ]

def prepare_disease(name, disease):
    df = read_owid(name)
    df["disease"] = disease
    return df[df["country"].isin(AFRO_COUNTRIES)].copy()

def outbreak_signals():
    p = RAW / "who_disease_outbreak_news.json"
    if not p.exists():
        return pd.DataFrame(columns=["title","publication_date","text","event_signal"])
    payload = json.loads(p.read_text())
    if isinstance(payload, dict):
        items = payload.get("value") or payload.get("items") or []
    else:
        items = payload
    rows = []
    diseases = r"cholera|measles|malaria|mpox|monkeypox|ebola|marburg|yellow fever|meningitis|polio|lassa|dengue|rift valley"
    for x in items:
        title = str(x.get("Title") or x.get("title") or "")
        summary = str(x.get("Summary") or x.get("summary") or x.get("Overview") or "")
        text = f"{title} {summary}"
        if not re.search(diseases, text, flags=re.I):
            continue
        rows.append({
            "title": title,
            "publication_date": x.get("PublicationDate") or x.get("publicationDate"),
            "text": text,
            "event_signal": 1.0
        })
    return pd.DataFrame(rows)

def latest_climate():
    """
    Load climate anomalies and select the latest usable observation
    for each country. Preserve missing data when no usable observation
    exists.
    """
    p = OUT / "climate_anomalies.csv"

    columns = [
        "iso3",
        "date",
        "temp_anomaly",
        "precip_anomaly_pct",
        "climate_component",
    ]

    if not p.exists():
        return pd.DataFrame(columns=columns)

    df = pd.read_csv(p)

    required = {
        "iso3",
        "date",
        "temp_anomaly_c",
        "precip_anomaly_pct",
        "climate_component",
    }

    missing = required.difference(df.columns)
    if missing:
        raise ValueError(
            f"Climate anomalies file is missing columns: {sorted(missing)}"
        )

    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    for column in [
        "temp_anomaly_c",
        "precip_anomaly_pct",
        "climate_component",
    ]:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    df = df.dropna(subset=["iso3", "date"]).copy()

    invalid = (
        df["climate_component"].notna()
        & ~df["climate_component"].between(0, 1)
    )

    if invalid.any():
        raise ValueError("Climate component values must be between 0 and 1.")

    duplicates = df.duplicated(["iso3", "date"], keep=False)
    if duplicates.any():
        sample = df.loc[duplicates, ["iso3", "date"]].head(10)
        raise ValueError(
            "Duplicate country-month records found. Investigate them "
            "before continuing:\\n" + sample.to_string(index=False)
        )

    # Exclude months with no usable climate component.
    usable = df.loc[df["climate_component"].notna()].copy()

    latest = (
        usable.sort_values("date")
        .groupby("iso3", as_index=False)
        .tail(1)
        .copy()
    )

    latest = latest.rename(
        columns={"temp_anomaly_c": "temp_anomaly"}
    )

    return latest[columns].copy()


def forecast(years, values, current_year=2026):
    """
    Produce a robust one-year-ahead baseline for annual disease data.

    Requires six consecutive annual observations and a latest observation
    no more than two years old. Uses the median of the last three values.
    This is a screening baseline, not a validated epidemiological model.
    """
    data = pd.DataFrame({
        "year": pd.to_numeric(pd.Series(years), errors="coerce"),
        "value": pd.to_numeric(pd.Series(values), errors="coerce"),
    })

    data = data.dropna(subset=["year", "value"]).copy()
    data = data.sort_values("year")

    if data.empty:
        return np.nan

    data = data[data["year"] % 1 == 0].copy()
    data["year"] = data["year"].astype(int)

    if data["year"].duplicated().any():
        return np.nan

    latest_year = int(data["year"].iloc[-1])

    if current_year - latest_year > 2 or latest_year > current_year:
        return np.nan

    recent = data.tail(6).copy()

    if len(recent) < 6:
        return np.nan

    if not recent["year"].diff().dropna().eq(1).all():
        return np.nan

    recent_values = recent["value"].astype("float64")

    if not np.isfinite(recent_values).all() or (recent_values < 0).any():
        return np.nan

    baseline = float(recent_values.tail(3).median())

    return max(0.0, baseline) if np.isfinite(baseline) else np.nan


def build():
    diseases = {
        "malaria_incidence": ("malaria_incidence", "Malaria"),
        "measles_cases": ("measles_cases", "Measles"),
        "cholera_cases": ("cholera_cases", "Cholera"),
    }
    all_disease = []
    for source, (file_name, disease) in diseases.items():
        all_disease.append(prepare_disease(file_name, disease))
    disease_df = pd.concat(all_disease, ignore_index=True)

    # Add vaccination coverage as context.
    vax = read_owid("measles_vax").rename(columns={"value":"measles_vax_pct"})
    disease_df = disease_df.merge(vax[["country","year","measles_vax_pct"]], on=["country","year"], how="left")

    results = []
    for (country, disease), g in disease_df.groupby(["country","disease"]):
        g = g.sort_values("year").copy()
        g["anomaly_score"] = robust_anomaly(g["value"])
        latest = g.iloc[-1]
        fc = forecast(g["year"], g["value"])
        prev = float(g["value"].iloc[-2]) if len(g) >= 2 else np.nan
        forecast_up = (np.nan if pd.isna(fc) else float(fc > float(latest["value"]) * 1.05))
        tr = trend_score(g["value"])
        vax = float(latest["measles_vax_pct"]) if disease == "Measles" and pd.notna(latest["measles_vax_pct"]) else np.nan

        results.append({
            "country": country,
            "iso3": latest["iso3"],
            "disease": disease,
            "latest_year": int(latest["year"]),
            "latest_value": float(latest["value"]),
            "anomaly_score": float(latest["anomaly_score"]),
            "trend_component": tr,
            "forecast_value": fc,
            "forecast_component": forecast_up,
            "measles_vax_pct": vax,
            "vax_gap_component": vaccination_gap(vax),
        })

    risk = pd.DataFrame(results)
    climate = latest_climate()

    if not climate.empty:
        risk = risk.merge(
            climate[
                [
                    "iso3",
                    "date",
                    "temp_anomaly",
                    "precip_anomaly_pct",
                    "climate_component",
                ]
            ],
            on="iso3",
            how="left",
            validate="many_to_one",
        )
        risk = risk.rename(columns={"date": "climate_observation_date"})
    else:
        risk["climate_observation_date"] = pd.NaT
        risk["temp_anomaly"] = np.nan
        risk["precip_anomaly_pct"] = np.nan
        risk["climate_component"] = np.nan

    events = outbreak_signals()
    event_count = len(events)
    # For MVP, event intelligence is a region-level signal. A future version should
    # extract country/disease entities using NER and join them at country-disease level.
    risk["event_component"] = 1.0 if event_count else 0.0

    risk["surveillance_freshness"] = risk["latest_year"].apply(surveillance_freshness)

    risk["evidence_freshness_status"] = (
        risk["surveillance_freshness"]
        .map({
            "Recent": "Recent surveillance",
            "Aging": "Review required",
            "Stale": "Review required",
            "Unknown": "Unknown freshness",
        })
        .fillna("Unknown freshness")
    )

    def forecast_warning(row):
        forecast = row["forecast_value"]
        latest = row["latest_value"]

        if pd.isna(forecast):
            return "No forecast available"
        if pd.isna(latest) or latest <= 0:
            return "Check baseline"
        if forecast / latest > 3:
            return "Review forecast"
        return "No large increase flagged"

    risk["forecast_warning"] = risk.apply(forecast_warning, axis=1)

    risk["risk_score"] = risk.apply(lambda r: risk_score(
        r["anomaly_score"], r["trend_component"], r["forecast_component"],
        r["vax_gap_component"], r["climate_component"], r["event_component"]
    ), axis=1)
    risk["risk_tier"] = risk["risk_score"].map(risk_tier)
    risk["explanation"] = risk.apply(explain, axis=1)

    risk = risk.sort_values("risk_score", ascending=False)
    risk.to_csv(OUT / "risk_register.csv", index=False)
    disease_df.to_csv(OUT / "disease_surveillance.csv", index=False)
    events.to_csv(OUT / "event_signals.csv", index=False)

    # Forecast table
    forecasts = risk[["country","iso3","disease","latest_year","latest_value","forecast_value"]].copy()
    forecasts.to_csv(OUT / "forecasts.csv", index=False)

    print(f"Built {len(risk):,} country-disease risk records.")
    print(risk.head(15).to_string(index=False))
    return risk

if __name__ == "__main__":
    build()
