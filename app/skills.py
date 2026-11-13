import yaml

def load_skills(path) -> list[str]:
    with open(path, encoding="utf-8") as f:
        skills_list = yaml.safe_load(f)
        return skills_list["skills"]

if __name__ == "__main__":
    print(load_skills("my_skills.yaml"))