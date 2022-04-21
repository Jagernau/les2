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

app.run()
