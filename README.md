Africa Public Health Intelligence & Early-Warning System

An end-to-end public-health analytics platform for disease surveillance, anomaly detection, baseline forecasting, climate context, and explainable risk prioritization across Africa.

""CI" (https://github.com/evanskips2727-del/Africa-Public-Health-Intelligence-/actions/workflows/ci.yml/badge.svg)" (https://github.com/evanskips2727-del/Africa-Public-Health-Intelligence-/actions/workflows/ci.yml)

Live Dashboard: "Explore the interactive application" (https://public-health-early-warning.streamlit.app/)

Repository: "View the source code" (https://github.com/evanskips2727-del/Africa-Public-Health-Intelligence-)

«Research and portfolio prototype: This application demonstrates public-health intelligence and analytical engineering techniques. Its risk scores and forecasts have not been validated for operational epidemiological use. The dashboard is not an official WHO system and must not be used as the sole basis for clinical, public-health emergency, or resource-allocation decisions.»

---

Overview

Public-health teams need to combine disease surveillance, historical trends, immunization indicators, environmental context, and outbreak reports to understand emerging risks.

This project demonstrates an end-to-end analytical workflow that integrates these information sources into a structured risk register and interactive dashboard.

Rather than presenting isolated charts, the system combines multiple signals to help analysts investigate country–disease combinations that may warrant further review.

Key capabilities

- Disease surveillance analytics: Examine historical disease observations and year-over-year changes.
- Robust anomaly detection: Identify unusual observations using rolling median and median absolute deviation (MAD).
- Baseline forecasting: Generate transparent one-year-ahead estimates using recent historical observations.
- Explainable risk scoring: Combine available surveillance, trend, forecast, vaccination, climate, and outbreak-event signals.
- Event-based intelligence: Extract structured signals from WHO Disease Outbreak News.
- Climate context: Incorporate temperature and precipitation information from NASA POWER.
- Data-quality and freshness checks: Identify records that require closer inspection because of missing, outdated, or questionable evidence.
- Interactive dashboard: Explore processed results through a Streamlit application.

Live Application

"Launch the Public Health Intelligence Dashboard" (https://public-health-early-warning.streamlit.app/)

The dashboard provides an interactive interface for exploring the project's analytical outputs.

The application is supported by a Python data pipeline, processed CSV datasets, and a risk-scoring engine.

Technical Architecture

Public Data Sources
        |
        v
Data Ingestion
        |
        v
Validation and Standardization
        |
        +-------------------+
        |                   |
        v                   v
Disease Surveillance    WHO Outbreak Events
        |                   |
        v                   v
Trend Analysis          Event Signal Extraction
        |
        +-------------------+
        |                   |
        v                   v
Anomaly Detection     Forecast Baseline
        |
        v
Climate and Vaccination Context
        |
        v
Explainable Risk-Scoring Engine
        |
        v
Processed Analytical Tables
        |
        v
Streamlit Dashboard

Technology stack

Area| Technologies
Programming| Python
Data manipulation| Pandas, NumPy
Statistical analysis| Median/MAD-based anomaly detection, time-series baselines
Machine learning and analytical utilities| Scikit-learn, Statsmodels
Data acquisition| Requests, public data APIs
Data storage| CSV, Parquet-compatible data tooling
Visualization and dashboard| Streamlit, Plotly
Automated testing| Pytest
Continuous integration| GitHub Actions
Development environment| Google Colab, local Python environments

Data Sources

The pipeline uses public data sources to construct its analytical datasets.

Source| Role in the project
WHO health indicators distributed through Our World in Data| Malaria incidence, reported measles and cholera cases, and measles vaccination coverage
WHO Disease Outbreak News API| Outbreak and public-health event signals
NASA POWER| Temperature and precipitation context for selected African country representative points
World Bank Indicators API| Population data used as a denominator where applicable

Data provenance matters: Our World in Data distributes health indicators whose original source may be WHO. The original provider, indicator definition, reporting period, units, and available coverage should be checked before drawing conclusions.

Publicly reported observations may be incomplete, revised, delayed, or inconsistent across countries and years. An absence of reported cases must not automatically be interpreted as an absence of disease.

Analytical Methodology

1. Disease Surveillance and Trend Analysis

The pipeline organizes disease observations into analytical tables that support historical comparisons and country–disease assessment.

The analysis includes annual observations and year-over-year changes where the underlying data supports these calculations.

2. Robust Anomaly Detection

The risk engine uses a rolling median and median absolute deviation to assess unusual observations.

Compared with a conventional mean-and-standard-deviation approach, this method can be less sensitive to extreme observations.

An anomaly is a statistical signal that deserves investigation. It does not, by itself, establish that an outbreak is occurring.

3. Baseline Forecasting

The forecasting component uses a transparent baseline based on the median of the last three annual observations.

The baseline requires six consecutive annual observations and a latest observation no more than two years old.

The forecast is intended for exploratory screening rather than validated epidemiological prediction. It does not establish causality or account for every factor that can influence disease transmission.

4. Explainable Risk Scoring

The prototype combines six analytical components:

Component| Weight
Disease anomaly| 30%
Disease trend| 20%
Forecast direction| 15%
Vaccination gap| 15%
Climate signal| 10%
Outbreak-event signal| 10%

The implementation excludes unavailable components and renormalizes the weights of the remaining components.

These weights are exploratory design choices, not empirically calibrated or epidemiologically validated parameters. The resulting score is a prioritization aid for human review, not a probability of an outbreak.

5. Risk Tiers

The prototype translates the combined score into four categories.

Score| Tier| Interpretation
0–24| Low| No strong combined signal under the prototype's scoring method
25–49| Moderate| Some signals warrant monitoring or further inspection
50–74| High| Multiple signals suggest closer analytical review
75–100| Critical| Strong combined signal requiring careful human review

These thresholds are project-defined and are not official WHO or WHO/AFRO classifications.

6. Event-Based Intelligence

The pipeline processes WHO Disease Outbreak News records and extracts structured signals using title and text keyword matching.

Keyword-based extraction is a lightweight method for organizing event information. It can miss relevant reports or flag items that need contextual interpretation.

7. Data Freshness and Quality

The analytical workflow includes checks for surveillance-data freshness and missing or questionable evidence.

Freshness categories help users distinguish recent observations from older information requiring review.

A recent observation is not necessarily complete or reliable, and an older observation is not automatically invalid. Interpretation depends on the reporting process, disease, and source.

Project Outputs

The pipeline produces structured datasets under "data/processed/":

File| Purpose
"disease_surveillance.csv"| Processed disease surveillance observations
"forecasts.csv"| Baseline forecast outputs
"climate_monthly_clean.csv"| Cleaned monthly climate observations
"climate_anomalies.csv"| Derived climate anomaly information
"event_signals.csv"| Structured outbreak-event signals
"risk_register.csv"| Combined country–disease risk assessments

These tables provide a reproducible analytical foundation for the dashboard and further investigation.

Repository Structure

Africa-Public-Health-Intelligence-/
├── .github/
│   └── workflows/
│       └── ci.yml
├── config/
│   └── countries.csv
├── data/
│   ├── raw/
│   └── processed/
├── docs/
│   └── PORTFOLIO_CASE_STUDY.md
├── scripts/
│   └── download_data.py
├── src/
│   ├── pipeline.py
│   └── risk_engine.py
├── tests/
│   └── test_risk.py
├── app.py
├── requirements.txt
└── README.md

The repository also contains a project notebook for exploratory development.

Getting Started

Prerequisites

- Python 3.11 or a compatible Python environment.
- Git, if cloning the repository.
- An internet connection for downloading source data.
- The dependencies listed in "requirements.txt".

1. Clone the repository

git clone https://github.com/evanskips2727-del/Africa-Public-Health-Intelligence-.git
cd Africa-Public-Health-Intelligence-

2. Create a virtual environment

python -m venv .venv

Activate it on Linux or macOS:

source .venv/bin/activate

On Windows:

.venv\Scripts\activate

3. Install dependencies

python -m pip install --upgrade pip
pip install -r requirements.txt
pip install pytest

4. Download source data

python scripts/download_data.py

This step retrieves the project's source data and stores downloaded files under "data/raw/", subject to source availability and network access.

5. Build the analytical tables

python -m src.pipeline

The pipeline processes the available data and generates analytical outputs under "data/processed/".

6. Run the automated tests

python -m pytest -q

The test suite checks selected risk-engine functionality. Passing tests do not constitute validation of epidemiological accuracy or operational readiness.

7. Launch the dashboard

streamlit run app.py

Streamlit will display a local address where the dashboard can be opened in a browser.

Execution note: Run the download and pipeline steps before launching the dashboard if the required processed datasets are not already present. Exact outputs depend on source availability and pipeline execution.

Continuous Integration

GitHub Actions runs the project's automated tests when changes are pushed to the configured branch or submitted through a pull request.

The workflow installs Python dependencies, installs Pytest, and executes the test suite.

Current CI status: "View workflow runs" (https://github.com/evanskips2727-del/Africa-Public-Health-Intelligence-/actions).

A successful CI run indicates that the configured tests passed in that environment. It does not establish that the risk scores or forecasts are epidemiologically valid.

Portfolio Highlights

This project demonstrates practical experience in:

- Building an end-to-end Python data pipeline.
- Integrating multiple public data sources.
- Cleaning, standardizing, and validating analytical datasets.
- Applying robust statistical methods to surveillance data.
- Designing transparent risk-scoring logic.
- Combining structured datasets and event-based information.
- Producing dashboard-ready analytical tables.
- Developing an interactive Streamlit application.
- Automating tests with GitHub Actions.
- Documenting analytical assumptions, limitations, and reproducible workflows.

The implementation connects data engineering, statistical analysis, and business-oriented presentation in a single portfolio project.

Limitations and Responsible Use

The project is an exploratory portfolio prototype, not an operational public-health surveillance service.

Important limitations include:

- Public data may be incomplete, delayed, revised, or inconsistent.
- Annual observations may be insufficient for timely outbreak detection.
- Forecasts use a simple historical baseline and have not been established as accurate predictive models.
- Risk-score weights and thresholds have not been calibrated against independently verified outbreak outcomes.
- Climate signals do not establish causal relationships with disease incidence.
- Keyword-based event extraction can produce missed signals or false positives.
- Country-level indicators can conceal important subnational differences.

The system should be interpreted as a demonstration of analytical methods and explainable prioritization, with human review required for interpretation.

It is not endorsed by WHO and must not be treated as an official disease alert, clinical decision-support tool, or substitute for established public-health reporting and response procedures.

Future Development

Potential extensions include:

1. Integrating higher-frequency surveillance data where reliable public access is available.
2. Adding subnational geospatial analysis.
3. Incorporating health-system readiness and preparedness indicators.
4. Evaluating forecasts through temporal backtesting and calibration.
5. Measuring anomaly-detection performance against independently verified events.
6. Adding data-quality monitoring and scheduled pipeline execution.
7. Expanding database support for larger analytical workloads.
8. Improving event extraction and evidence traceability.
9. Adding automated monitoring of data-source freshness.
10. Evaluating the risk-scoring approach with domain experts and documented validation criteria.

Author

Evans Kiplangat

Data Analytics | Data Engineering | Applied Statistics

- "GitHub" (https://github.com/evans25575)
- "LinkedIn" (https://linkedin.com/in/evans-kiplangat-375646179)
- "Live Project Dashboard" (https://public-health-early-warning.streamlit.app/)

---

Built as a portfolio project demonstrating reproducible data engineering, statistical analysis, explainable risk assessment, and interactive public-health analytics.
