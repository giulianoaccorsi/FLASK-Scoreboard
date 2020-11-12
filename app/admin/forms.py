from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Length


class TeamForm(FlaskForm):
    name = StringField("Nome do time", validators=[DataRequired(), Length(min=1, max=30)])
    acronym = StringField("Acrônimo do time", validators=[DataRequired(), Length(min=1, max=10)])
    local = StringField("Local", validators=[DataRequired(), Length(min=1, max=30)])
    submit = SubmitField("Enviar")


class MatchForm(FlaskForm):
    home_team = StringField("Time da casa", validators=[DataRequired()])
    guest_team = StringField("Time visitante", validators=[DataRequired()])
    home_points = StringField("Placar da casa", validators=[DataRequired(), Length(min=1, max=3)])
    guest_points = StringField("Placar do visitante", validators=[DataRequired(), Length(min=1, max=3)])
    submit = SubmitField("Enviar")
