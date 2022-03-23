def load_candidates_from_json(path):
    candidate_list = []
    for index in path:
        candidate_list.append({'id': index['id'], "name": index['name']})
    return candidate_list


def get_candidate(candidate_id, data):
    for index in data:
        if index['id'] == int(candidate_id):
            return index


def get_candidates_by_name(candidate_name, data):
    candidates = []
    for index in data:
        if candidate_name.lower() in index['name'].lower():
            candidates.append({'id': index['id'], "name": index['name']})
    return candidates


def get_candidates_by_skill(skill_name, data):
    candidates = []
    for index in data:
        if skill_name.lower() in index['skills'].lower():
            candidates.append({'id': index['id'], "name": index['name']})
    return candidates


