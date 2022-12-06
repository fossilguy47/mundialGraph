import numpy as np
from flask import Flask, flash, request, render_template, redirect

from .forms import *
from .models.team import *



app = Flask(__name__)

if __name__ == "__main__":
    app.run()


@app.route("/")
def home():
    return render_template('home.html')


@app.route('/team/index', methods=['GET', 'POST'])
def index_team():
    results = Team.index()
    items = []
    for result in results:
        items += result[0].values()
    return render_template('team/index.html', items=items)


@app.route('/team/add/', methods=['GET', 'POST'])
def add_team():
    form = AddTeamForm()
    if request.method == "POST":
        if form.is_submitted():
            result = request.form
            name = result['name']
            if Team(name).add():
                flash(f"Added {name} team")
            else:
                flash(f"{name} team is already in the database")

    return render_template('team/add.html', form=form)


@app.route('/team/delete/', methods=['GET', 'POST'])
def delete_team():
    form = DeleteTeamForm()
    if request.method == "POST":
        if form.is_submitted():
            result = request.form
            name = result['name']
            if Team(name).delete():
                flash(f"Deleted {name} team")
            else:
                flash(f"{name} team was not in the database")

    return render_template('team/delete.html', form=form)





@app.route('/team/duel/', methods=['GET', 'POST'])
def duel_team():
    form = DuelTeamForm()
    if request.method == "POST":
        if form.is_submitted():
            result = request.form
            name = result['name']
            team_name = result['team_name']
            duel_result = result['duel_result']
            if Team(name).duel(Team(team_name), duel_result):
                flash(f"{name} is in duel with {team_name}")
            else:
                flash(f"{name} or {team_name} does not exist")

    return render_template('team/duel.html', form=form)


@app.route('/team/duel_info/', methods=['GET', 'POST'])
def duel_infoover():
    form = DuelInfoTeamForm()
    if request.method == "POST":
        if form.is_submitted():
            result = request.form
            name = result['name']
            results = Team(name).duel_info()
            if results is False or None in results[0]:
                flash(f"No duel information for {name}")
            else:
                items = []
                for result in results:
                    for r in result:
                        items += r.values()
                items = np.reshape(items, (-1, 3))
                return render_template('team/duel_info_index.html', items=items)

    return render_template('team/duel_info.html', form=form)



