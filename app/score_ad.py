from app.parser import parse_job_ad
from app.scorer import fit_score
from app.skills import load_skills

if __name__ == "__main__":
    path = "tests/ads/03_volkswagen.txt"
    with open(path, encoding="utf-8") as f:
        text = f.read()
    ad = parse_job_ad(text)
    my_skills = load_skills("my_skills.yaml")
    ad_skills = ad.skills
    print(fit_score(ad_skills, my_skills))
