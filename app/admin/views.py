from . import admin
from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from .utils import admin_required, distribute_points_win_loss_draw
from app.models import Team, Match
from app import db
from .forms import TeamForm, MatchForm
from sqlalchemy.exc import IntegrityError as IE


@admin.route("/")
@login_required
@admin_required
def home():
    return render_template("admin/dashboard.html")


@admin.route("/equipes")
@login_required
@admin_required
def teams():
    teams = Team.query.all()
    return render_template("admin/teams/teams.html", teams=teams, title="Times")


@admin.route("/equipes/criar", methods=["GET", "POST"])
@login_required
@admin_required
def create_team():
    creating_team = True
    form = TeamForm()
    if form.validate_on_submit():
        team = Team(name=form.name.data,
                    acronym=form.acronym.data,
                    local=form.local.data
                    )
        try:
            db.session.add(team)
            db.session.commit()
            flash("Time cadastrado com sucesso!", "success")
        except IE:
            flash("O nome e/ou acrônimo já existem!", "error")
            db.session.rollback()
        finally:
            db.session.close()

        return redirect(url_for("admin.teams"))
    return render_template("admin/teams/team.html",
                           form=form,
                           creating_team=creating_team,
                           title="Cadastrar time")


@admin.route("/equipes/alterar/<int:id>", methods=["GET", "POST"])
@login_required
@admin_required
def edit_team(id):
    creating_team = False
    team = Team.query.get_or_404(id)
    form = TeamForm(obj=team)
    if form.validate_on_submit():
        team.name = form.name.data
        team.acronym = form.acronym.data
        team.local = form.local.data
        db.session.commit()
        flash("Time alterado com sucesso!", "success")
        return redirect(url_for("admin.teams"))

    form.name.data = team.name
    form.acronym.data = team.acronym
    form.local.data = team.local

    return render_template("admin/teams/team.html",
                           creating_team=creating_team,
                           form=form,
                           team=team,
                           title="Editando time")


@admin.route("/equipes/deletar/<int:id>")
@login_required
@admin_required
def delete_team(id):
    team = Team.query.get_or_404(id)
    db.session.delete(team)
    db.session.commit()
    db.session.close()
    flash("Time deletado com sucesso!", "success")

    return redirect(url_for("admin.teams"))


@admin.route("/partidas")
@login_required
@admin_required
def matchs():
    matchs = Match.query.all()
    return render_template("admin/matchs/matchs.html", matchs=matchs, title="Partidas")


@admin.route("/partidas/criar", methods=["GET", "POST"])
@login_required
@admin_required
def create_match():
    creating_match = True
    form = MatchForm()
    if form.validate_on_submit():
        match = Match(home_team=form.home_team.data,
                      guest_team=form.guest_team.data,
                      home_points=form.home_points.data,
                      guest_points=form.guest_points.data,
                      )
        try:
            db.session.add(match)
            db.session.commit()
            flash("Partida cadastrada com sucesso!", "success")
        except Exception as e:
            flash(f"{e}", "error")
            db.session.rollback()
        finally:
            db.session.close()

        return redirect(url_for("admin.matchs"))
    return render_template("admin/matchs/match.html",
                           form=form,
                           creating_match=creating_match,
                           title="Cadastrar partida")


@admin.route("/partidas/alterar/<int:id>", methods=["GET", "POST"])
@login_required
@admin_required
def edit_match(id):
    creating_match = False
    match = Match.query.get_or_404(id)
    form = MatchForm(obj=match)
    if form.validate_on_submit():
        match.home_team = form.home_team.data
        match.guest_team = form.guest_team.data
        match.home_points = form.home_points.data
        match.guest_points = form.guest_points.data
        db.session.commit()
        flash("Partida alterado com sucesso!", "success")
        return redirect(url_for("admin.matchs"))

    form.home_team.data = match.home_team
    form.guest_team.data = match.guest_team
    form.home_points.data = match.home_points
    form.guest_points.data = match.guest_points

    return render_template("admin/matchs/match.html",
                           creating_match=creating_match,
                           form=form,
                           match=match,
                           title="Editando Partida")


@admin.route("/partidas/deletar/<int:id>")
@login_required
@admin_required
def delete_match(id):
    match = Match.query.get_or_404(id)
    db.session.delete(match)
    db.session.commit()
    db.session.close()
    flash("Partida deletada com sucesso!", "success")

    return redirect(url_for("admin.matchs"))



