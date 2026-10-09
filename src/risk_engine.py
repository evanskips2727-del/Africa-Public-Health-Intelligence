import numpy as np
import pandas as pd

RISK_BANDS = [
    (0, 25, "Low"),
    (25, 50, "Moderate"),
    (50, 75, "High"),
    (75, 101, "Critical"),
]

def robust_anomaly(series, window=5):
    """Robust rolling anomaly using median absolute deviation."""
    s = pd.Series(series, dtype="float64")
    med = s.rolling(window, min_periods=3).median()
    mad = (s - med).abs().rolling(window, min_periods=3).median()
    score = (s - med).abs() / (1.4826 * mad.replace(0, np.nan))
    return score.replace([np.inf, -np.inf], np.nan).fillna(0)

def trend_score(series, periods=3):
    """Score recent upward movement relative to a recent baseline."""
    s = pd.Series(series, dtype="float64").dropna()
    if len(s) < periods + 2:
        return 0.0
    recent = s.tail(periods).mean()
    baseline = s.iloc[-periods-3:-periods].mean() if len(s) >= periods + 3 else s.iloc[:-periods].mean()
    if baseline <= 0 or pd.isna(baseline):
        return 0.0
    pct = (recent - baseline) / baseline
    return float(np.clip((pct + 0.25) / 0.75, 0, 1))

def vaccination_gap(vax_percent):
    """Return a normalized vaccination gap, preserving missing values."""
    if pd.isna(vax_percent):
        return np.nan
    return float(np.clip((95 - vax_percent) / 50, 0, 1))


def climate_signal(temp_anomaly=None, precip_anomaly=None):
    """Summarize available climate anomalies; preserve missing observations."""
    vals = []

    if pd.notna(temp_anomaly):
        vals.append(np.clip(abs(temp_anomaly) / 3, 0, 1))

    if pd.notna(precip_anomaly):
        vals.append(np.clip(abs(precip_anomaly) / 100, 0, 1))

    return float(np.mean(vals)) if vals else np.nan


def risk_score(anomaly, trend, forecast_up, vax_gap, climate, event_signal):
    """
    Calculate an explainable screening score from available components.

    Missing components are excluded, and the remaining weights are
    renormalized. Weights are exploratory portfolio-demo choices,
    not validated public-health risk weights.
    """
    components = [
        (anomaly, 0.30, lambda value: value / 4),
        (trend, 0.20, lambda value: value),
        (forecast_up, 0.15, lambda value: value),
        (vax_gap, 0.15, lambda value: value),
        (climate, 0.10, lambda value: value),
        (event_signal, 0.10, lambda value: value),
    ]

    weighted_sum = 0.0
    available_weight = 0.0

    for value, weight, transform in components:
        if value is None:
            continue

        try:
            value = float(value)
        except (TypeError, ValueError):
            continue

        if not np.isfinite(value):
            continue

        normalized = float(np.clip(transform(value), 0, 1))

        weighted_sum += weight * normalized
        available_weight += weight

    if available_weight == 0:
        return np.nan

    score = 100 * weighted_sum / available_weight
    return round(float(np.clip(score, 0, 100)), 1)


def surveillance_freshness(latest_year, current_year=2026):
    """Classify the age of the latest annual surveillance observation."""
    try:
        year = float(latest_year)
    except (TypeError, ValueError):
        return "Unknown"

    if not np.isfinite(year) or year % 1 != 0:
        return "Unknown"

    year = int(year)

    if year > current_year or year < 1900:
        return "Unknown"

    age = current_year - year

    if age <= 2:
        return "Recent"
    if age <= 4:
        return "Aging"
    return "Stale"


def risk_tier(score):
    for lo, hi, label in RISK_BANDS:
        if lo <= score < hi:
            return label
    return "Critical"

def explain(row):
    reasons = []
    if row.get("anomaly_score", 0) >= 2:
        reasons.append("recent surveillance anomaly")
    if row.get("trend_component", 0) >= 0.6:
        reasons.append("rising recent trend")
    if row.get("forecast_component", 0) >= 0.6:
        reasons.append("forecast points upward")
    if row.get("vax_gap_component", 0) >= 0.5:
        reasons.append("immunization gap")
    if row.get("climate_component", 0) >= 0.5:
        reasons.append("unusual climate conditions")
    if row.get("event_component", 0) >= 0.5:
        reasons.append("recent outbreak intelligence signal")
    return "; ".join(reasons) if reasons else "no strong converging signal"
