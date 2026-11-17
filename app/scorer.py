def fit_score(ad_skills: list[str], my_skills: list[str]) -> tuple[set[str], set[str], int]: 
    ad = set(s.lower() for s in ad_skills)
    myskills = set(s.lower() for s in my_skills)
     
    matched = myskills & ad
    missing = ad - myskills
    if not ad:
        return set(), set(), 0
    score = round(len(matched) / len(ad) * 100)
    
    return matched, missing, score


def normalize(skills: list[str], alias_map: dict[str, str]) -> list[str]:
    skills_normalised = []
    for s in skills:
        skills_normalised.append(alias_map.get(s.lower(), s.lower()))
    return skills_normalised

