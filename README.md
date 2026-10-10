## Africa Public Health Intelligence Platform

**An Open-Source Disease Surveillance and Early-Warning Analytics Prototype for Africa

""Python" (https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)" (https://www.python.org/)
""Streamlit" (https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit&logoColor=white)" (https://streamlit.io/)
""Pandas" (https://img.shields.io/badge/Data-Pandas-150458?logo=pandas&logoColor=white)" (https://pandas.pydata.org/)
""License" (https://img.shields.io/badge/License-MIT-green.svg)" (LICENSE)

Africa Public Health Intelligence Platform is a data engineering and public health analytics project that integrates disease surveillance indicators, vaccination coverage, climate observations, and outbreak-related information into an interactive early-warning dashboard.

The platform demonstrates how multi-source public health data can be collected, cleaned, validated, transformed, analyzed, and translated into explainable risk-prioritization signals.

Live Dashboard

"Launch the Interactive Dashboard" (https://public-health-early-warning.streamlit.app/)

"Explore the Source Code" (https://github.com/evanskips2727-del/Africa-Public-Health-Intelligence)

---

Project Overview

Public health surveillance requires reliable data integration, consistent data quality, and timely interpretation of multiple indicators. Data may originate from different organizations, use different reporting formats, or have different levels of completeness.

This project addresses these analytical challenges through a reproducible Python pipeline and an interactive dashboard designed to support exploration of disease indicators across African countries.

Key Capabilities

- Multi-source data integration: Combines disease indicators, measles vaccination coverage, climate observations, and outbreak-related information.
- Data cleaning and validation: Standardizes data types, handles sentinel missing values, checks climate measurements, and identifies duplicate country-month records.
- Statistical anomaly detection: Uses rolling medians and median absolute deviation to identify unusual observations.
- Trend analysis: Compares recent disease observations with historical baseline values.
- Forecasting: Uses exponential smoothing with a damped trend where sufficient observations are available.
- Composite risk scoring: Combines multiple analytical indicators into a bounded score from 0 to 100.
- Interactive visualization: Presents country-disease signals and risk categories through a Streamlit dashboard.
- Automated testing: Includes unit tests for risk-score bounds, risk-tier assignment, and vaccination-gap behavior.

---

Dashboard Preview

Explore the deployed application:

"Open the Live Dashboard" (https://public-health-early-warning.streamlit.app/)

The dashboard supports interactive exploration of country-disease signals and their associated analytical risk scores.

---

Data Sources

The pipeline integrates publicly available datasets and services.

Source| Data Used| Analytical Purpose
Our World in Data| Malaria incidence, reported measles cases, cholera cases, and measles vaccination coverage| Disease surveillance indicators and vaccination context
World Health Organization| Disease Outbreak News| Outbreak-related contextual signals
NASA POWER| Temperature and precipitation observations| Climate anomaly analysis
World Bank| Population data| Supplementary demographic data availability

Data source documentation: See ""data/SOURCES.md"" (data/SOURCES.md) for source details and data acquisition notes.

Data availability, coverage, reporting frequency, and geographic resolution vary by source and indicator.

---

Data Engineering and Quality Management

A core component of this project is preparing heterogeneous source data for consistent downstream analysis.

Data Preparation

The pipeline includes:

- Conversion of date fields into consistent datetime representations.
- Conversion of analytical variables into numeric formats.
- Treatment of sentinel values such as "-999" as missing climate observations.
- Validation of climate measurements and exclusion of invalid records.
- Checks for negative precipitation values.
- Removal of climate records without valid country or date identifiers.
- Duplicate checks for country-month climate observations.
- Standardization and alignment of country, date, and disease indicators before analysis.

These steps improve the consistency of the analytical dataset and reduce the risk of invalid observations propagating into downstream calculations.

Missing Data

Missing values are handled according to the processing requirements of individual indicators. The availability of an input signal can affect the resulting composite risk score; therefore, scores should be interpreted alongside the available evidence and data limitations.

---

Analytical Methodology

The platform combines several analytical components to produce a composite risk-prioritization score.

1. Statistical Anomaly Detection

The anomaly component uses a rolling median and median absolute deviation (MAD) to identify observations that differ from recent historical patterns.

This robust statistical approach reduces sensitivity to extreme observations compared with methods that rely only on the mean and standard deviation.

2. Trend Analysis

Recent observations are compared with earlier baseline observations to estimate the direction and magnitude of changes in disease indicators.

3. Forecasting

The pipeline uses exponential smoothing with an additive damped trend when sufficient historical observations are available.

If model fitting fails, the pipeline can fall back to the mean of the most recent three observations. Forecast availability depends on the length and quality of the historical series.

4. Vaccination Coverage Gap

For measles, the vaccination-gap component compares available coverage against a reference level of 95%.

The component is bounded between 0 and 1. Its interpretation depends on the availability and quality of the underlying vaccination data.

5. Climate Anomaly Analysis

Temperature and precipitation observations are evaluated against historical climate baselines to derive climate-related signals.

Climate observations are based on representative geographic points rather than nationally representative measurements. Consequently, they should not be interpreted as complete descriptions of national climate conditions.

6. Outbreak-Related Context

WHO Disease Outbreak News is processed to identify relevant outbreak-related information.

This component provides contextual information rather than a fully validated country-specific disease-event linkage.

---

Composite Risk Scoring

The risk engine combines six components into a score ranging from 0 to 100.

Component| Weight
Statistical anomaly| 30%
Disease trend| 20%
Forecast signal| 15%
Vaccination coverage gap| 15%
Climate signal| 10%
Outbreak-related context| 10%
Total| 100%

The component weights represent the prototype's analytical design. They should not be interpreted as clinically validated or epidemiologically calibrated parameters.

Risk Categories

Score| Category
0–<25| Low
25–<50| Moderate
50–<75| High
75–100| Critical

The resulting score is an analytical prioritization signal, not a validated probability of an outbreak.

Unavailable or incomplete input signals can affect the composite score. Users should review data availability and source limitations before drawing conclusions from individual country-disease results.

---

Technology Stack

Area| Technologies
Programming| Python
Data manipulation| Pandas, NumPy
Statistical analysis| SciPy-compatible statistical methods, Statsmodels
Data acquisition| Requests, public data endpoints
Visualization| Plotly
Dashboard| Streamlit
Machine learning and forecasting ecosystem| Scikit-learn, Statsmodels
Testing| Pytest
Version control| Git and GitHub
Deployment| Streamlit Community Cloud

---

System Architecture

Public Data Sources
        |
        v
Data Acquisition
        |
        v
Cleaning and Validation
        |
        v
Feature Engineering
        |
        v
Anomaly Detection, Trend Analysis
and Forecasting
        |
        v
Composite Risk Scoring
        |
        v
Country-Disease Risk Signals
        |
        v
Interactive Streamlit Dashboard

---

Repository Structure

Africa-Public-Health-Intelligence/
├── app.py
├── src/
│   ├── pipeline.py
│   └── risk_engine.py
├── config/
│   └── countries.csv
├── scripts/
│   └── download_data.py
├── tests/
│   └── test_risk.py
├── docs/
│   └── PORTFOLIO_CASE_STUDY.md
├── data/
│   └── SOURCES.md
├── notebooks/
├── requirements.txt
├── .github/
│   └── workflows/
└── README.md

The exact contents of optional directories may change as the project develops.

---

Installation and Local Setup

Prerequisites

- Python 3.10 or later
- Git
- Internet access for downloading source data

1. Clone the Repository

git clone https://github.com/evanskips2727-del/Africa-Public-Health-Intelligence.git
cd Africa-Public-Health-Intelligence

2. Create a Virtual Environment

python -m venv .venv

Activate it on Linux or macOS:

source .venv/bin/activate

On Windows:

.venv\Scripts\activate

3. Install Dependencies

python -m pip install --upgrade pip
pip install -r requirements.txt

4. Download or Refresh Data

Run the project's data acquisition script:

python scripts/download_data.py

5. Launch the Dashboard

streamlit run app.py

Streamlit will provide a local address for opening the application in your browser.

Note: Successful execution depends on the current repository configuration, dependency compatibility, and availability of the upstream data sources.

---

Testing

The repository includes unit tests for core risk-engine behavior.

Run the tests with:

python -m pytest -q

The tests cover areas including:

- Composite score bounds.
- Risk-category assignment.
- Vaccination-gap behavior.

These tests provide focused checks of selected risk-engine functions. They do not, by themselves, establish that the complete data pipeline is error-free or that the risk model is epidemiologically validated.

---

Limitations and Responsible Interpretation

This project is an independent analytical prototype intended for learning, demonstration, and portfolio evaluation.

- Not an official surveillance system: It is not an official WHO or WHO AFRO product and is not endorsed by those organizations.
- Not an outbreak declaration tool: Scores are heuristic prioritization signals, not validated outbreak probabilities or official classifications.
- Source coverage varies: Data completeness, reporting frequency, and historical coverage differ across indicators and countries.
- Climate representativeness is limited: Representative geographic points do not capture all within-country climate variation.
- Event matching is limited: Outbreak-related information is not guaranteed to be matched precisely to every country-disease record.
- Missing inputs affect scores: Incomplete data can influence the composite score and its interpretation.
- Forecasts are conditional: Forecast quality depends on the length, consistency, and reliability of historical observations.
- Further validation is required: The scoring design requires epidemiological review, calibration, backtesting, and evaluation against appropriate reference outcomes before any operational use.

The platform should be used for analytical exploration and demonstration—not clinical decision-making, emergency response decisions, or official public health reporting.

---

Future Development

Potential improvements include:

- Expanding automated data-quality monitoring and pipeline observability.
- Improving country-specific outbreak-event matching.
- Incorporating population-normalized indicators where appropriate and supported by source data.
- Evaluating alternative anomaly-detection and forecasting approaches.
- Adding historical backtesting and model-performance reporting.
- Improving documentation of input completeness and score provenance.
- Expanding automated test coverage and continuous integration.
- Seeking domain-expert review of risk-score design and epidemiological assumptions.

---

Project Documentation

- "Live Dashboard" (https://public-health-early-warning.streamlit.app/)
- "GitHub Repository" (https://github.com/evanskips2727-del/Africa-Public-Health-Intelligence)
- "Portfolio Case Study" (docs/PORTFOLIO_CASE_STUDY.md)
- "Data Sources and Acquisition Notes" (data/SOURCES.md)

---

About the Author

Evans Kiplangat
Data Analyst | Data Engineer | Public Health Analytics

I build data pipelines, analytical dashboards, and data-driven tools that turn complex datasets into structured, interpretable insights.

My technical interests include data engineering, statistical analysis, business intelligence, machine learning, monitoring and evaluation, and digital public health.

- GitHub: "evans25575" (https://github.com/evans25575)
- LinkedIn: "Evans Kiplangat" (https://linkedin.com/in/evans-kiplangat-375646179)
- Portfolio: "View Portfolio" (https://evans25575.github.io/Evans---portfolio/)

---

License

This project is licensed under the MIT License, subject to the repository's ""LICENSE"" (LICENSE) file.

---

Built as an independent portfolio project demonstrating data engineering, statistical analysis, data quality management, and public health intelligence workflows.
