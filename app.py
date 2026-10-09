from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

ROOT = Path(__file__).resolve().parent
RISK = ROOT / "data" / "processed" / "risk_register.csv"
SURV = ROOT / "data" / "processed" / "disease_surveillance.csv"
EVENTS = ROOT / "data" / "processed" / "event_signals.csv"

st.set_page_config(page_title="Africa Public Health Intelligence", layout="wide")

st.title("Africa Public Health Intelligence & Early-Warning System")
st.caption("Portfolio prototype — surveillance, signals, forecasting and explainable risk prioritization")

if not RISK.exists():
    st.warning("No processed data found. Run `python scripts/download_data.py` then `python -m src.pipeline`.")
    st.stop()

risk = pd.read_csv(RISK)
surv = pd.read_csv(SURV)
events = pd.read_csv(EVENTS) if EVENTS.exists() else pd.DataFrame()

# Sidebar
st.sidebar.header("Filters")
diseases = sorted(risk["disease"].dropna().unique())
disease = st.sidebar.selectbox("Disease", ["All"] + diseases)
tiers = ["Critical", "High", "Moderate", "Low"]
tier = st.sidebar.selectbox("Risk tier", ["All"] + tiers)

view = risk.copy()
if disease != "All":
    view = view[view["disease"] == disease]
if tier != "All":
    view = view[view["risk_tier"] == tier]

c1, c2, c3, c4 = st.columns(4)
c1.metric("Country-disease signals", len(view))
c2.metric("Critical", int((view.risk_tier == "Critical").sum()))
c3.metric("High", int((view.risk_tier == "High").sum()))
c4.metric("WHO event records", len(events))

st.subheader("Priority risk register")
st.dataframe(
    view[[
        "country","disease","latest_year","latest_value","risk_score",
        "risk_tier","forecast_value","explanation"
    ]].head(30),
    use_container_width=True,
    hide_index=True
)

st.subheader("Risk landscape")
fig = px.bar(
    view.head(20).sort_values("risk_score"),
    x="risk_score", y="country", color="risk_tier",
    orientation="h", facet_col="disease",
    title="Top prioritized signals"
)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Surveillance trend")
country = st.selectbox("Country", sorted(surv.country.unique()))
trend = surv[surv.country == country].copy()
if disease != "All":
    trend = trend[trend.disease == disease]

fig2 = px.line(
    trend, x="year", y="value", color="disease",
    markers=True, title=f"Annual surveillance indicators — {country}"
)
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Decision-support interpretation")
if len(view):
    selected = st.selectbox(
        "Select a prioritized signal",
        [f"{r.country} — {r.disease}" for _, r in view.head(20).iterrows()]
    )
    country_name, disease_name = selected.split(" — ", 1)
    row = view[(view.country == country_name) & (view.disease == disease_name)].iloc[0]
    st.info(
        f"**{row.country} / {row.disease}: {row.risk_tier} ({row.risk_score}/100).** "
        f"{row.explanation}. "
        "This is a prioritization signal for human review, not a diagnosis or confirmed outbreak."
    )

with st.expander("Methodology and limitations"):
    st.markdown("""
**Risk score components**

- 30% recent robust surveillance anomaly
- 20% recent upward trend
- 15% forecast direction
- 15% measles immunization gap
- 10% climate anomaly
- 10% event-based WHO signal

These are **portfolio-demo weights**, not WHO weights.

**Major limitation:** the current surveillance layer is primarily annual country-level data. A production early-warning system needs weekly/subnational surveillance, reporting completeness, laboratory signals, population mobility, health-system readiness and validated epidemiological models.
""")

st.caption("Data provenance: WHO / WHO AFRO, Our World in Data, NASA POWER, World Bank. This project is independent and not endorsed by WHO.")
