from json import load

with open("candidates.json", encoding="utf-8") as f:
    names = load(f)


def load_candidates_from_json():
    """список кандидатов"""
    return names

def get_candidate(candidate_id):
    """возвращает одного кандидата по его id"""
    for i in names:
        if i["id"] == int(candidate_id):
            return i

def get_candidates_by_name(candidate_name):
    """возвращает кандидатов по имени"""
    for i in names:
        if i["name"] == str(candidate_name).capitalize:
            return i

def get_candidates_by_skill(skill_name):
    """возвращает кандидатов по навыку"""
    cand = []
    for i in names:
        if str(skill_name).capitalize() in i["skills"].split(", "):
            cand.append(i)
        if str(skill_name) in i["skills"].split(", "):
            cand.append(i)
    return cand



