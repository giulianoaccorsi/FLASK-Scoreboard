from . import website
from flask import render_template
from flask_login import login_required
from sqlalchemy import desc
from app.admin.utils import distribute_points_win_loss_draw
from app.models import Team, Match


@login_required
@website.route("/painel")
def dashboard():
    matches = Match.query.all()
    distribute_points_win_loss_draw(matches)
    teams = Team.query.order_by(desc(Team.points)).all()
    return render_template("website/dashboard.html", teams=teams)


@website.route("/")
def index():
    return render_template("website/home.html", title="Bem vindo!")


@website.route("/detalhes/<int:id>")
def details(id):
    team = Team.query.filter_by(id=id).first_or_404()
    matches_home_team = Match.query.filter_by(home_team=team.name).all()
    matches_guest_team = Match.query.filter_by(guest_team=team.name).all()
    for match in matches_guest_team:
        matches_home_team.append(match)
    return render_template("website/details.html", matches=matches_home_team)

