import json
from pathlib import Path
import time
import requests
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
RAW.mkdir(parents=True, exist_ok=True)

HEADERS = {"User-Agent": "Africa-Public-Health-Intelligence-Portfolio/1.0"}

OWID = {
    "malaria_incidence": "https://ourworldindata.org/grapher/incidence-of-malaria.csv?v=1&csvType=full&useColumnShortNames=false",
    "measles_cases": "https://ourworldindata.org/grapher/reported-cases-of-measles.csv?v=1&csvType=full&useColumnShortNames=false",
    "cholera_cases": "https://ourworldindata.org/grapher/number-reported-cases-of-cholera.csv?v=1&csvType=full&useColumnShortNames=false",
    "measles_vax": "https://ourworldindata.org/grapher/share-of-children-vaccinated-against-measles.csv?v=1&csvType=full&useColumnShortNames=false",
}

def download_csv(name, url):
    path = RAW / f"{name}.csv"
    print(f"Downloading {name}...")
    r = requests.get(url, headers=HEADERS, timeout=60)
    r.raise_for_status()
    path.write_bytes(r.content)
    print(f"  saved {path} ({len(r.content):,} bytes)")
    return path

def download_world_bank_population():
    url = "https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json&per_page=20000"
    path = RAW / "population_world_bank.json"
    print("Downloading population...")
    r = requests.get(url, headers=HEADERS, timeout=60)
    r.raise_for_status()
    path.write_bytes(r.content)
    return path

def download_who_outbreak_news():
    url = "https://www.who.int/api/default/diseaseoutbreaknews"
    path = RAW / "who_disease_outbreak_news.json"
    print("Downloading WHO Disease Outbreak News...")
    r = requests.get(url, headers=HEADERS, timeout=60)
    r.raise_for_status()
    path.write_bytes(r.content)
    return path

def nasa_monthly(lat, lon, start="20150101", end="20261231"):
    url = (
        "https://power.larc.nasa.gov/api/temporal/monthly/point"
        f"?parameters=T2M,PRECTOTCORR&community=RE"
        f"&longitude={lon}&latitude={lat}&start=2015&end=2026&format=JSON"
    )
    r = requests.get(url, headers=HEADERS, timeout=60)
    r.raise_for_status()
    return r.json()

def download_nasa_climate():
    countries = pd.read_csv(ROOT / "config" / "countries.csv")
    out = []
    for _, row in countries.iterrows():
        print(f"Downloading climate: {row.country}")
        try:
            payload = nasa_monthly(row.latitude, row.longitude)
            params = payload.get("properties", {}).get("parameter", {})
            dates = set()
            for p in params.values():
                dates.update(p.keys())
            for date in sorted(dates):
                out.append({
                    "country": row.country,
                    "iso3": row.iso3,
                    "date": date,
                    "temperature_c": params.get("T2M", {}).get(date),
                    "precipitation_mm": params.get("PRECTOTCORR", {}).get(date),
                })
        except Exception as exc:
            print(f"  WARNING: {exc}")
        time.sleep(0.25)

    pd.DataFrame(out).to_csv(RAW / "nasa_climate_monthly.csv", index=False)

if __name__ == "__main__":
    for name, url in OWID.items():
        download_csv(name, url)

    download_world_bank_population()
    download_who_outbreak_news()
    download_nasa_climate()
    print("\nAll available downloads completed.")
