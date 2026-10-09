import pandas as pd
from src.risk_engine import risk_score, risk_tier, vaccination_gap

def test_risk_score_bounds():
    assert 0 <= risk_score(10, 1, 1, 1, 1, 1) <= 100

def test_risk_tiers():
    assert risk_tier(10) == "Low"
    assert risk_tier(40) == "Moderate"
    assert risk_tier(60) == "High"
    assert risk_tier(90) == "Critical"

def test_vaccination_gap():
    assert vaccination_gap(95) == 0
    assert vaccination_gap(45) == 1
