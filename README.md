# Africa Public Health Intelligence & Early-Warning Prototype

**Portfolio project:** Africa Public Health Intelligence & Early-Warning System  
**Positioning:** Public-health surveillance + risk analytics + anomaly detection + forecasting + climate context + event-based signals + explainable decision support.

> This is a portfolio/research prototype inspired by the kinds of capabilities used in public-health intelligence and preparedness systems. It is **not** a validated outbreak prediction system and must not be used for clinical or emergency decisions.

## Why this project exists

The goal is to demonstrate that a data practitioner can move beyond a static health dashboard and build an end-to-end intelligence workflow:

**Data ingestion → validation → surveillance analytics → anomaly detection → forecast → contextual risk scoring → event signals → decision-oriented dashboard**

The design is intentionally aligned with public-health intelligence concepts: early signal detection, risk assessment, situational awareness, evidence synthesis, and explainable prioritization.

## Data sources

The download pipeline uses reproducible public sources:

1. **WHO Global Health Observatory data via Our World in Data**
   - Malaria incidence
   - Reported measles cases
   - Reported cholera cases
   - Measles vaccination coverage
2. **WHO Disease Outbreak News API**
   - Event-based outbreak/public-health signals
3. **NASA POWER**
   - Temperature and precipitation context for selected African country representative points
4. **World Bank Indicators API**
   - Population denominator

The OWID mirrors used in the project document WHO as the original health-data provider. Always inspect the source metadata before publishing a new analysis.

## Core analytical outputs

### 1. Surveillance trend
Annual disease burden and year-over-year change.

### 2. Anomaly detection
Rolling median/MAD-based anomaly score:

- robust to extreme values
- interpretable
- less sensitive to outliers than ordinary z-scores

### 3. Forecast
A transparent one-year-ahead baseline uses the median of the last three annual observations. It requires six consecutive annual observations and a latest observation no more than two years old. This is a screening baseline, not a validated epidemiological forecasting model. The project treats forecasting as a **signal**, not a certainty.

### 4. Contextual risk score
The prototype combines:

- recent disease anomaly
- upward trend
- forecast direction
- vaccination gap
- climate anomaly
- recent outbreak/news signal

The score is deliberately interpretable so an analyst can explain why a country-disease pair was prioritized.

### 5. Event-based intelligence
WHO Disease Outbreak News records are converted into structured signals using title/text keyword extraction.

## Risk interpretation

| Score | Tier | Interpretation |
|---:|---|---|
| 0–24 | Low | No strong combined signal |
| 25–49 | Moderate | One or more contextual signals |
| 50–74 | High | Multiple converging signals |
| 75–100 | Critical | Strong convergence; requires human review |

**Important:** The score is a portfolio prototype, not a WHO/AFRO risk classification.

## Project architecture

```text
                    ┌──────────────────────┐
                    │ WHO / OWID datasets  │
                    └──────────┬───────────┘
                               │
                    ┌──────────▼───────────┐
                    │ Data ingestion layer │
                    │ validation + schema  │
                    └──────────┬───────────┘
                               │
          ┌────────────────────┼─────────────────────┐
          │                    │                     │
 ┌────────▼────────┐  ┌────────▼────────┐  ┌────────▼─────────┐
 │ Disease trends  │  │ WHO event       │  │ Climate context  │
 │ + anomalies     │  │ intelligence    │  │ NASA POWER       │
 └────────┬────────┘  └────────┬────────┘  └────────┬─────────┘
          │                    │                     │
          └────────────────────┼─────────────────────┘
                               │
                    ┌──────────▼───────────┐
                    │ Explainable risk     │
                    │ scoring engine       │
                    └──────────┬───────────┘
                               │
                    ┌──────────▼───────────┐
                    │ Streamlit intelligence│
                    │ dashboard             │
                    └──────────────────────┘
```

## Run locally

### 1. Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Termux:

```bash
pkg update
pkg install python
pip install -r requirements.txt
```

### 2. Download data

```bash
python scripts/download_data.py
```

This creates files under `data/raw/`.

### 3. Build analytical tables

```bash
python -m src.pipeline
```

### 4. Launch

```bash
streamlit run app.py
```

If Streamlit is too heavy for the phone, run the pipeline first and use the generated CSVs for a lightweight portfolio notebook/dashboard. The analytical core is independent of Streamlit.

## Suggested portfolio title

**Africa Public Health Intelligence & Early-Warning System**

Alternative:

**Public Health Threat Intelligence & Outbreak Early-Warning Prototype**

## Strong portfolio claims you can make

- Built an end-to-end public-health intelligence pipeline integrating WHO disease surveillance, WHO outbreak signals, climate context and immunization indicators.
- Implemented robust anomaly detection and transparent multi-factor risk scoring to prioritize country-disease signals for human review.
- Added baseline time-series forecasting and event-based intelligence extraction to move from retrospective reporting toward early-warning analytics.
- Designed an explainable dashboard showing the evidence behind each risk tier rather than presenting an opaque model output.

## Claims you should NOT make

Do not claim:

- WHO endorsement
- PDX replication
- operational outbreak prediction
- validated epidemiological forecasting
- causal climate-disease relationships
- deployment in a ministry/WHO system
- clinical decision support

## Next-level extensions

1. Replace annual surveillance with weekly IDSR/EWARS data.
2. Add subnational geospatial data.
3. Add health-system readiness indicators.
4. Add IHR/JEE preparedness indicators.
5. Add laboratory/genomic signals.
6. Add cross-border transmission/network features.
7. Add retrieval-augmented AI explanations with source citations.
8. Add model backtesting and calibration.
9. Add PostgreSQL/PostGIS + dbt.
10. Add automated scheduled ingestion and data-quality monitoring.
