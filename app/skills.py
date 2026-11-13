import yaml

def load_skills(path) -> list[str]:
    with open(path, encoding="utf-8") as f:
        skills_list = yaml.safe_load(f)
        return skills_list["skills"]

def load_aliases(path) -> dict[str, str]:
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    alias_map = {}
    for main, aliases in data.items():
        for alias in aliases or []:
            alias_map[alias] = main
    return alias_map

if __name__ == "__main__":
    print(load_skills("my_skills.yaml"))
    print(load_aliases("skill_aliases.yaml"))