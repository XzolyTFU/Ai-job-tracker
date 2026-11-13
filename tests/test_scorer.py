import pytest
from app.scorer import fit_score

def test_partial_match():
    matched, missing, score = fit_score(["C", "Python", "Docker"], ["c", "python"])
    assert score == 67
    assert missing == {"Docker".lower()}

def test_case_insensitive():
    matched, missing, score = fit_score(["C", "Python", "Docker"], ["c", "PYThon", "DOcKER"])
    assert score == 100
    assert not missing

def test_no_skills():
    matched, missing, score = fit_score([], ["c", "python"])
    assert score == 0