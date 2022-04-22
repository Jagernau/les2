import functions as fu
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def general():
    """страница с сылками на кандидатов"""
    candidates = fu.load_candidates_from_json()
    return render_template("list.html", cand=candidates)

@app.route('/candidate/<x>')
def candidat(x):
    """страница кандидата по id"""
    candidat = fu.get_candidate(x)
    return render_template("card.html", data=candidat)

@app.route('/search/<candidate_name>')
def name(candidate_name):
    """страница кондидатов по имени"""
    names = fu.get_candidates_by_name(candidate_name)
    count = len(names)
    return render_template("search.html", nam=names, cou=count )
@app.route('/skill/<skill_name>')
def skill(skill_name):
    skill = fu.get_candidates_by_skill(skill_name)
    count = len(skill)
    enter = skill_name
    return render_template("skill.html", ski=skill, cou=count, ent=enter)

app.run()
