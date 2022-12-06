from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class AddTeamForm(FlaskForm):
    name = StringField("Team name")
    submit = SubmitField("Add")


class DeleteTeamForm(FlaskForm):
    name = StringField("Team name")
    submit = SubmitField("Delete")



class DuelTeamForm(FlaskForm):
    name = StringField("Team name")
    team_name = StringField("2nd team name")
    duel_result = StringField("Result")
    submit = SubmitField("Add")


class DuelInfoTeamForm(FlaskForm):
    name = StringField("Team name")
    submit = SubmitField("Info")


