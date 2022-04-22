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
    nam = []
    for i in names:        
        if str(candidate_name).upper() in i["name"].upper().split(" "):
            nam.append(i)
    return nam

def get_candidates_by_skill(skill_name):
    """возвращает кандидатов по навыку"""
    cand = []
    for i in names:
        if str(skill_name).upper() in i["skills"].upper().split(", "):
            cand.append(i)
    return cand



