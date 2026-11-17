import pytest
from app.scorer import fit_score, normalize

def test_normalize():
    alias_map = {"c++": "cpp", "golang": "go"}
    result = normalize(["C++", "Python", "GoLang"], alias_map)
    assert result == ["cpp", "python", "go"]