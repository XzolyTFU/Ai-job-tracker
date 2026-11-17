from app.parser import parse_job_ad
from app.scorer import fit_score, normalize
from app.skills import load_skills, load_aliases


if __name__ == "__main__":
    path = "tests/ads/03_volkswagen.txt"
    with open(path, encoding="utf-8") as f:
        text = f.read()
    ad = parse_job_ad(text)
    my_skills = load_skills("my_skills.yaml")
    alias_map = load_aliases("skill_aliases.yaml")
    ad_skills = ad.skills
    normalized_my_skills = normalize(my_skills, alias_map)
    normalized_ad_skills = normalize(ad_skills, alias_map)
    print(fit_score(normalized_ad_skills, normalized_my_skills))
