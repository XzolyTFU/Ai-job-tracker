import pytest
from pathlib import Path
from app.parser import parse_job_ad


ADS = sorted(Path("tests/ads").glob("*.txt"))

@pytest.mark.parametrize("path", ADS, ids=lambda p: p.name)
def test_parse_job_ad(path):
    text = open(path, encoding="utf-8").read()
    ad = parse_job_ad(text)
    assert ad.company
    assert ad.title
    assert ad.location
    assert ad.company in text
    assert len(ad.skills) > 0
    if ad.posted_at:
        assert ad.posted_at.year >= 2025

@pytest.mark.parametrize("path", ADS, ids=lambda p: p.name)
def test_skills_appear_in_ad(path):
    text = open(path, encoding="utf-8").read()
    ad = parse_job_ad(text)
    if len(ad.skills) > 0:
        for skill in ad.skills:
            assert skill.lower() in text.lower(), f"{skill} not found in the ad"