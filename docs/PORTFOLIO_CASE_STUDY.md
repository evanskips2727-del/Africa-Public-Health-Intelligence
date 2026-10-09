# Portfolio case study

## Problem

Public-health teams need to move from retrospective reporting toward earlier identification of signals that may require investigation.

A useful intelligence workflow must combine multiple evidence streams rather than rely on a single disease chart.

## Solution

I built an Africa-focused public-health intelligence prototype that integrates:

- WHO-derived disease surveillance
- WHO event-based outbreak intelligence
- immunization coverage
- climate context
- population data
- robust anomaly detection
- baseline forecasting
- explainable multi-factor risk prioritization

## What makes it more than a dashboard

The system produces a **risk register** rather than only visualizations.

Each country-disease record contains:

- latest surveillance value
- robust anomaly score
- recent trend component
- forecast direction
- immunization-gap component
- climate component
- event-based intelligence signal
- composite risk score
- human-readable explanation

## Example decision question

> Which country-disease signals deserve analyst attention first?

The system ranks signals and explains the evidence contributing to the priority.

## Technical stack

Python, Pandas, NumPy, scikit-learn, Statsmodels, Plotly, Streamlit, REST APIs, GitHub Actions.

## Public-health relevance

This project demonstrates applied data engineering, surveillance analytics, anomaly detection, forecasting, explainability and decision-support design in a public-health context.

It intentionally does not claim epidemiological validation or operational deployment.

## Next production step

The highest-value improvement is replacing annual country-level indicators with weekly IDSR/EWARS or equivalent surveillance data and adding reporting completeness, subnational geography, laboratory signals and health-system readiness.
