from flask import Flask, render_template, url_for
from load_data import data
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

add = Flask(__name__)


@add.route("/")
def home_page():
    candidates_lists = load_candidates_from_json(data)
    return render_template('lists.html', items=candidates_lists)


@add.route('/candidate/<x>/')
def page_candidate(x):
    cand = get_candidate(int(x), data)
    return render_template('single.html', cand=cand)


@add.route('/search/<candidate_name>/')
def page_name_candidate(candidate_name):
    name = get_candidates_by_name(candidate_name, data)
    return render_template('search.html', names=name, len=len(name))


@add.route('/skill/<skill_name>/')
def page_skills(skill_name):
    skills = get_candidates_by_skill(skill_name, data)
    return render_template('skill.html', skills=skills, len=len(skills), search_skill=skill_name)


if __name__ in "__main__":
    add.run()


