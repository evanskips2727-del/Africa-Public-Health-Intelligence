## Africa Public Health Intelligence

# An Explainable Disease Surveillance Analytics & Early-Warning Prototype

Transforming public-health data into structured surveillance insights through data engineering, statistical anomaly detection, baseline forecasting, climate analysis, and explainable risk prioritization.

<p align="center">
  <a href="https://public-health-early-warning.streamlit.app/">
    <img src="https://img.shields.io/badge/Live%20Dashboard-Explore%20Application-2E8B57?style=for-the-badge&logo=streamlit&logoColor=white" alt="Explore Live Dashboard">
  </a>
  <a href="https://github.com/evanskips2727-del/Africa-Public-Health-Intelligence-/actions/workflows/ci.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/evanskips2727-del/Africa-Public-Health-Intelligence-/ci.yml?branch=main&style=for-the-badge&label=CI%20Status" alt="Continuous Integration Status">
  </a>
  <a href="https://github.com/evanskips2727-del/Africa-Public-Health-Intelligence-/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-See%20Repository%20Files-blue?style=for-the-badge" alt="License Information">
  </a>
</p><p align="center">
  <strong>Python</strong> · <strong>Pandas</strong> · <strong>Statistical Analysis</strong> · <strong>Data Engineering</strong> · <strong>Streamlit</strong> · <strong>Plotly</strong> · <strong>GitHub Actions</strong>
</p>---

Table of Contents
Table of Contents

- "Project Overview" (#project-overview)
- "Live Application" (#live-application)
- "The Problem" (#the-problem)
- "Project Objectives" (#project-objectives)
- "Core Capabilities" (#core-capabilities)
- "System Architecture" (#system-architecture)
- "Technology Stack" (#technology-stack)
- "Data Sources" (#data-sources)
- "Analytical Methodology" (#analytical-methodology)
- "Risk Assessment Framework" (#risk-assessment-framework)
- "Analytical Outputs" (#analytical-outputs)
- "Repository Structure" (#repository-structure)
- "Getting Started" (#getting-started)
- "Continuous Integration and Testing" (#continuous-integration-and-testing)
- "Data Quality and Responsible Use" (#data-quality-and-responsible-use)
- "Project Limitations" (#project-limitations)
- "Future Development Roadmap" (#future-development-roadmap)
- "Skills Demonstrated" (#skills-demonstrated)
- "Author" (#author)
- "Disclaimer" (#disclaimer)

Project Overview

Africa Public Health Intelligence is an end-to-end public-health analytics project designed to demonstrate how heterogeneous public datasets can be transformed into structured analytical outputs for disease surveillance and exploratory risk assessment.

The platform integrates disease observations, historical trends, vaccination indicators, climate context, population data, and reported outbreak events into a unified analytical workflow.

Using Python-based data processing, robust statistical methods, transparent forecasting baselines, and an explainable risk-scoring engine, the system generates country–disease assessments that can be explored through an interactive Streamlit dashboard.

Rather than presenting disconnected charts, the project demonstrates a complete analytical lifecycle:

Data acquisition → Data validation → Transformation → Statistical analysis → Risk assessment → Interactive visualization

The implementation brings together data engineering, applied statistics, analytical development, and public-health intelligence in one reproducible portfolio project.

«Project classification: Research and portfolio prototype. Forecasts, anomaly indicators, and composite risk scores are exploratory analytical outputs and have not been validated for operational epidemiological use.»

Live Application

Explore the Interactive Dashboard

"Launch Africa Public Health Intelligence Dashboard" (https://public-health-early-warning.streamlit.app/)

The application provides an interface for exploring processed public-health intelligence outputs.

The analytical workflow is supported by Python scripts, processed datasets, statistical methods, and an explainable risk-assessment engine.

"View the Source Code on GitHub" (https://github.com/evanskips2727-del/Africa-Public-Health-Intelligence-) · "View Continuous Integration Runs" (https://github.com/evanskips2727-del/Africa-Public-Health-Intelligence-/actions)

Note: The availability of the live application and its displayed results depends on the deployment environment and the datasets available to the application.

---

The Problem

Public-health analysis frequently requires information from multiple sources with different reporting periods, data structures, geographic coverage, and levels of completeness.

Analyzing these datasets independently can make it difficult to compare historical disease patterns, identify unusual observations, assess vaccination gaps, incorporate environmental context, and organize outbreak-related information.

This project addresses the analytical integration challenge by bringing multiple indicators into a consistent workflow.

The objective is to demonstrate how public data can be processed into interpretable, traceable outputs that support further investigation by human analysts.

The platform does not replace epidemiological expertise, official reporting systems, or established public-health surveillance procedures.

Project Objectives

The project is designed to:

1. Integrate public-health and environmental datasets from multiple public sources.
2. Establish a reproducible pipeline for downloading, cleaning, transforming, and standardizing data.
3. Identify statistically unusual disease observations using robust anomaly-detection techniques.
4. Generate transparent baseline forecasts from historical observations.
5. Incorporate vaccination, climate, and outbreak-event indicators into a common analytical framework.
6. Produce explainable country–disease risk assessments.
7. Monitor selected aspects of data freshness and quality.
8. Publish analytical outputs through an interactive dashboard.
9. Apply automated testing and continuous integration to support software reliability.

---

Core Capabilities

Capability| Implementation| Analytical Purpose
Disease surveillance analytics| Historical observations and year-over-year comparisons| Examine disease patterns over time
Data engineering| Python-based ingestion and transformation| Standardize heterogeneous public datasets
Anomaly detection| Rolling median and median absolute deviation (MAD)| Identify unusual observations
Baseline forecasting| Median of recent annual observations| Establish an exploratory reference for future analysis
Explainable risk assessment| Weighted composite scoring| Organize multiple analytical signals
Vaccination-gap analysis| Measles vaccination coverage indicators| Incorporate immunization context
Climate intelligence| Temperature and precipitation observations| Examine environmental context
Event-based intelligence| WHO Disease Outbreak News and keyword-based extraction| Structure information from outbreak reports
Data quality monitoring| Freshness, missing-data, and evidence checks| Flag observations requiring closer inspection
Interactive visualization| Streamlit and Plotly| Explore analytical outputs
Automated testing| Pytest and GitHub Actions| Test selected software functionality

---

System Architecture

The system follows a modular analytical workflow that separates data acquisition, processing, statistical analysis, risk assessment, and presentation.

             PUBLIC DATA SOURCES
                      |
                      v
              DATA ACQUISITION
       APIs, downloaded datasets, public feeds
                      |
                      v
            DATA VALIDATION LAYER
       Schema checks, missing values, standardization
                      |
                      v
           ANALYTICAL DATA PIPELINE
                      |
          +-----------+-----------+
          |           |           |
          v           v           v
       Disease      Climate     Outbreak
       Trends       Context      Events
          |           |           |
          v           v           v
      Anomaly      Climate     Event Signal
      Detection    Analysis    Extraction
          |           |           |
          +-----------+-----------+
                      |
                      v
            FORECASTING BASELINES
                      |
                      v
          EXPLAINABLE RISK ENGINE
                      |
                      v
             PROCESSED DATASETS
                      |
                      v
          INTERACTIVE STREAMLIT APP
                      |
                      v
            HUMAN ANALYST REVIEW

Architectural Principles

- Modularity: Separate data-processing, analytical, and presentation responsibilities.
- Reproducibility: Use documented scripts and consistent processing steps.
- Transparency: Expose the assumptions behind anomaly detection, forecasting, and risk scoring.
- Traceability: Retain structured analytical outputs for inspection.
- Responsible interpretation: Distinguish statistical signals from verified epidemiological events.

---

Technology Stack

Category| Technologies
Programming| Python
Data manipulation| Pandas, NumPy
Statistical analysis| Rolling median, median absolute deviation, historical baselines
Analytical utilities| Scikit-learn, Statsmodels
Data acquisition| Requests, public data APIs
Data formats| CSV and related tabular data tooling
Dashboard development| Streamlit
Data visualization| Plotly
Automated testing| Pytest
Continuous integration| GitHub Actions
Development environments| Google Colab and compatible local Python environments
Version control| Git and GitHub

The table describes the project's documented technology stack. Actual usage of individual dependencies depends on the relevant modules and execution paths.

---

Data Sources

The analytical workflow uses public data sources to construct disease surveillance, environmental, demographic, and event-based datasets.

Data Source| Role in the Project
Our World in Data health datasets| Access to selected disease-incidence, reported-case, and vaccination indicators
WHO Disease Outbreak News| Public-health event information and outbreak-related signals
NASA POWER| Temperature and precipitation context for selected country representative points
World Bank Indicators API| Population indicators used as denominators where applicable

Data Provenance

Data provenance is essential when combining public-health indicators.

For example, Our World in Data may redistribute indicators originally published by WHO or other organizations. The distribution platform should not automatically be treated as the original data producer.

Before interpreting a result, users should examine:

- The original data provider.
- The indicator definition and measurement units.
- The reporting period and geographic coverage.
- The completeness and timeliness of the observations.
- Any documented revisions or methodological changes.

An observation that is missing from a dataset does not establish that the corresponding disease or event was absent.

Source availability and API behavior may change over time. Reproducing the workflow therefore depends on network access, source availability, and the current structure of the upstream datasets.

---

Analytical Methodology

1. Disease Surveillance and Trend Analysis

The pipeline organizes disease observations into analytical tables suitable for historical comparison and country–disease assessment.

Depending on the availability and structure of the underlying indicators, the workflow supports:

- Historical disease-observation analysis.
- Annual comparisons.
- Year-over-year changes.
- Identification of observations requiring additional investigation.

The resulting tables provide a foundation for the downstream anomaly-detection, forecasting, and risk-assessment components.

2. Robust Anomaly Detection

The prototype uses a rolling median and median absolute deviation (MAD) to identify observations that differ from their surrounding historical patterns.

The median provides a robust measure of central tendency, while MAD measures the typical absolute deviation from that median.

Compared with a conventional mean-and-standard-deviation approach, these statistics can be less sensitive to extreme observations.

The objective is to flag unusual data points for further investigation.

Interpretation: A statistical anomaly is not, by itself, evidence of an outbreak. Reporting changes, data-quality issues, revisions, and other factors may also produce unusual observations.

3. Baseline Forecasting

The forecasting component establishes a simple historical reference using the median of the last three annual observations.

The documented baseline requirements are:

- At least six consecutive annual observations.
- A most recent observation no more than two years old.
- Sufficient historical data to calculate the baseline.

The resulting estimate provides a transparent reference for exploratory analysis.

It is not a validated epidemiological prediction model and does not account for every factor that can influence disease transmission.

Forecast interpretation must consider historical data quality, reporting delays, structural changes, and the limitations of annual observations.

4. Climate Context

The project incorporates temperature and precipitation information from NASA POWER for selected representative points associated with African countries.

These indicators provide environmental context for examining disease-related patterns.

Climate observations are contextual features, not proof of a causal relationship between weather conditions and disease incidence.

Country-level representative points also cannot capture all local environmental variation.

5. Vaccination-Gap Analysis

Selected vaccination indicators, including measles vaccination coverage, provide additional context for the risk-assessment workflow.

Vaccination coverage can help analysts examine potential immunization gaps alongside disease observations and other available indicators.

Interpretation depends on the indicator definition, reporting period, population coverage, and completeness of the source data.

6. Event-Based Intelligence

The workflow processes WHO Disease Outbreak News records and extracts structured event signals using keyword matching against available titles and text.

This approach provides a lightweight method for organizing outbreak-related information alongside quantitative surveillance indicators.

Keyword extraction has limitations:

- Relevant events may not contain the expected terms.
- A keyword match may not indicate a confirmed outbreak in a particular country.
- Historical reports may refer to events that are no longer active.
- Context and geographic relevance require human interpretation.

Extracted signals should therefore be treated as supporting evidence rather than verified outbreak classifications.

7. Data Freshness and Quality Assessment

The project includes checks intended to flag observations that may require additional scrutiny because of missing information, questionable values, or outdated reporting.

Freshness indicators help distinguish recently reported observations from older records.

However, freshness alone does not establish reliability. Recent observations may be incomplete, while older observations may remain useful for historical analysis.

Data-quality findings should be interpreted in the context of the source, indicator, reporting process, and intended analytical use.

---

Risk Assessment Framework

Explainable Composite Scoring

The prototype combines six analytical components into a composite score intended to prioritize country–disease combinations for further review.

Component| Weight| Analytical Contribution
Disease anomaly| 30%| Identifies unusual disease observations
Disease trend| 20%| Represents the direction of historical change
Forecast direction| 15%| Incorporates the baseline forecast signal
Vaccination gap| 15%| Adds immunization-related context
Climate signal| 10%| Incorporates environmental indicators
Outbreak-event signal| 10%| Adds information extracted from outbreak reports
Total| 100%| 

The implementation excludes unavailable components and renormalizes the weights of the remaining components.

This design allows the prototype to produce an assessment when some indicators are unavailable, while making the resulting score dependent on the evidence actually present.

Risk Tiers

The composite score is mapped to four project-defined categories.

Score| Category| Interpretation
0–24| Low| No strong combined signal under the prototype's scoring method
25–49| Moderate| Some indicators warrant monitoring or further inspection
50–74| High| Multiple signals warrant closer analytical review
75–100| Critical| A strong combined signal warrants careful human review

These categories are intended to make the output easier to interpret and investigate.

Important Methodological Considerations

The scoring weights and thresholds are exploratory design choices.

They have not been empirically calibrated against independently verified outbreak outcomes or established as epidemiologically valid decision thresholds.

Consequently:

- The score is not a probability of an outbreak.
- A high score does not confirm an outbreak.
- A low score does not establish the absence of disease risk.
- Comparisons between countries may be affected by differences in reporting completeness and indicator availability.
- Risk tiers are not official WHO or WHO/AFRO classifications.

The intended use is explainable analytical prioritization with human review, not automated public-health decision-making.

---

Analytical Outputs

The pipeline produces structured analytical datasets under "data/processed/".

Output File| Purpose
"disease_surveillance.csv"| Processed disease surveillance observations
"forecasts.csv"| Baseline forecast outputs
"climate_monthly_clean.csv"| Cleaned monthly climate observations
"climate_anomalies.csv"| Derived climate-anomaly information
"event_signals.csv"| Structured signals extracted from outbreak-related reports
"risk_register.csv"| Combined country–disease risk assessments

These files provide a structured foundation for the dashboard and further analytical investigation.

Execution note: The availability of individual outputs depends on successful data acquisition, pipeline execution, and the upstream sources used by the relevant processing steps.

---

Repository Structure

Africa-Public-Health-Intelligence-/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── config/
│   └── countries.csv
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│   └── PORTFOLIO_CASE_STUDY.md
│
├── scripts/
│   └── download_data.py
│
├── src/
│   ├── pipeline.py
│   └── risk_engine.py
│
├── tests/
│   └── test_risk.py
│
├── Africa_Public_Health_Intelligence.ipynb
├── app.py
├── requirements.txt
└── README.md

Key Components

Component| Responsibility
"config/"| Country configuration and supporting reference data
"data/raw/"| Downloaded or source-level datasets
"data/processed/"| Transformed datasets and analytical outputs
"docs/"| Project documentation and case study
"scripts/download_data.py"| Data acquisition workflow
"src/pipeline.py"| Main analytical pipeline
"src/risk_engine.py"| Risk-assessment functionality
"tests/"| Automated tests
"app.py"| Streamlit application entry point
"requirements.txt"| Python dependency definitions
"Africa_Public_Health_Intelligence.ipynb"| Exploratory development notebook
".github/workflows/ci.yml"| Continuous integration workflow

---

Getting Started

Follow these instructions to run the project in a compatible Python environment.

Prerequisites

- Python 3.11 or another Python version supported by the project's dependencies.
- Git.
- Internet access for downloading public datasets.
- A compatible environment with sufficient resources to install the dependencies.
- The packages specified in "requirements.txt".

1. Clone the Repository

git clone https://github.com/evanskips2727-del/Africa-Public-Health-Intelligence-.git

cd Africa-Public-Health-Intelligence-

2. Create a Virtual Environment

python -m venv .venv

Linux or macOS:

source .venv/bin/activate

Windows PowerShell:

.\.venv\Scripts\Activate.ps1

3. Install Dependencies

Upgrade pip and install the project dependencies:

python -m pip install --upgrade pip

python -m pip install -r requirements.txt

python -m pip install pytest

If dependency installation fails, check the Python version and the compatibility of the affected package.

4. Download the Source Data

python scripts/download_data.py

This command runs the project's data-acquisition script.

Downloaded datasets are expected to be stored under "data/raw/", subject to the implementation and availability of the upstream sources.

5. Run the Analytical Pipeline

python -m src.pipeline

The pipeline processes the available source data and generates analytical outputs under "data/processed/".

Review the execution output for missing inputs, network errors, or processing failures.

6. Run Automated Tests

python -m pytest -q

The test suite checks selected functionality implemented in the project.

Passing tests demonstrate that the tested code meets the assertions defined by the test suite. They do not establish the epidemiological accuracy of the analytical outputs.

7. Launch the Dashboard

streamlit run app.py

Streamlit will display a local address that can be opened in a browser.

Recommended execution order: Install dependencies, download the data, execute the pipeline, run the tests, and then launch the dashboard.

The exact outputs depend on source availability, the local environment, and successful pipeline execution.

---

Continuous Integration and Testing

The repository includes a GitHub Actions workflow at ".github/workflows/ci.yml".

The workflow is intended to automate software checks when changes are pushed to the configured branch or submitted through a pull request.

The documented workflow installs the required dependencies, installs Pytest, and runs the automated test suite.

Check the CI Status

"View GitHub Actions Workflow Runs" (https://github.com/evanskips2727-del/Africa-Public-Health-Intelligence-/actions)

A successful workflow run indicates that the configured checks passed in that execution environment.

It does not guarantee that every data source is accessible, that every pipeline output is complete, or that the risk-assessment methodology is epidemiologically valid.

---

Data Quality and Responsible Use

Public-health datasets require careful interpretation because data availability and reporting practices vary.

The project is designed to make analytical assumptions more visible and to organize evidence for further review.

When interpreting outputs, consider:

- Missing or delayed observations.
- Differences in country-level reporting practices.
- Revisions to historical data.
- Changes in indicator definitions.
- Inconsistent geographic or temporal coverage.
- Potential bias introduced by incomplete evidence.
- The difference between a statistical signal and a confirmed epidemiological event.

Where possible, decisions should be informed by the original data source, documented indicator definitions, domain expertise, and independently verified evidence.

---

Project Limitations

This project is an exploratory analytics prototype rather than an operational disease surveillance service.

Its principal limitations include:

1. Data completeness: Public datasets may be incomplete, delayed, revised, or inconsistent.
2. Temporal resolution: Annual observations may be insufficient for timely outbreak detection.
3. Forecast validation: The historical-median baseline has not been established as an accurate predictive model.
4. Risk-score calibration: Composite weights and tier thresholds have not been validated against independently verified outbreak outcomes.
5. Climate interpretation: Environmental associations do not establish causation.
6. Event extraction: Keyword-based methods may produce false positives or miss relevant reports.
7. Geographic granularity: Country-level indicators may conceal important subnational variation.
8. Operational readiness: The prototype has not been established as suitable for clinical, emergency-response, or resource-allocation decisions.

These limitations define the appropriate scope of the project: demonstrating analytical engineering and transparent exploratory risk assessment.

---

Future Development Roadmap

Potential extensions include:

- [ ] Integrate higher-frequency surveillance data where reliable access is available.
- [ ] Introduce subnational geospatial analysis.
- [ ] Add health-system readiness and preparedness indicators.
- [ ] Evaluate forecast performance using temporal backtesting.
- [ ] Assess anomaly-detection performance against independently verified events.
- [ ] Implement scheduled data acquisition and pipeline execution.
- [ ] Expand data-quality checks and source-freshness monitoring.
- [ ] Improve event extraction and evidence traceability.
- [ ] Evaluate database support for larger analytical workloads.
- [ ] Engage public-health domain experts to define validation criteria and assess the risk-scoring methodology.

Future development should prioritize measurable analytical performance, reproducibility, data provenance, and responsible interpretation.

---

Skills Demonstrated

This project brings together practical concepts from data engineering, applied statistics, analytics, and application development.

Data Engineering

- Public-data acquisition and API integration.
- Data cleaning and standardization.
- Structured data transformation.
- Analytical pipeline development.
- Processed dataset generation.

Applied Statistics and Analytics

- Historical trend analysis.
- Robust anomaly detection using median and MAD.
- Transparent baseline forecasting.
- Composite indicator design.
- Explainable risk assessment.
- Data-quality interpretation.

Data Visualization and Applications

- Interactive dashboard development.
- Analytical result presentation.
- Structured data exploration.
- Dashboard-oriented data preparation.

Software Engineering

- Modular Python code.
- Repository organization.
- Automated testing with Pytest.
- Continuous integration with GitHub Actions.
- Technical documentation.
- Reproducible execution instructions.

The project demonstrates how these disciplines can be connected in a single analytical workflow, from public data acquisition through processing and statistical analysis to interactive presentation.

---

Author

Evans Kiplangat

Data Analytics | Data Engineering | Applied Statistics

- GitHub: "@evans25575" (https://github.com/evans25575)
- LinkedIn: "Evans Kiplangat" (https://linkedin.com/in/evans-kiplangat-375646179)
- Live Application: "Africa Public Health Intelligence Dashboard" (https://public-health-early-warning.streamlit.app/)
- Project Repository: "Africa Public Health Intelligence" (https://github.com/evanskips2727-del/Africa-Public-Health-Intelligence-)

---

Disclaimer

Africa Public Health Intelligence is an independent research and portfolio project.

It is not an official World Health Organization system, is not endorsed by WHO or WHO/AFRO, and is not intended to replace established public-health surveillance systems.

The forecasts, anomaly indicators, event signals, and composite risk scores are exploratory analytical outputs that have not been validated for operational epidemiological use.

Do not use this application as the sole basis for clinical decisions, outbreak declarations, emergency responses, or public-health resource allocation. Decisions of this nature require appropriate expert review, verified evidence, and established public-health procedures.

---

<p align="center">
  <strong>Built to demonstrate reproducible data engineering, applied statistical analysis, explainable risk assessment, and interactive public-health analytics.</strong>
</p>
