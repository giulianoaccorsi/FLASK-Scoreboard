from flask import flash, redirect, url_for
from functools import wraps
from flask_login import current_user
from app.models import Team


def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        admin = current_user.is_admin
        if not admin:
            flash("Você precisa ser admin para acessar este recurso")
            return redirect(url_for('website.dashboard'))
        return f(*args, **kwargs)
    return decorated


def distribute_points_win_loss_draw(obj):
    for match in obj:
        home_team = Team.query.filter_by(name=match.home_team).first()
        guest_team = Team.query.filter_by(name=match.guest_team).first()
        if not home_team or not guest_team:
            flash("Nenhuma partida encontrada")
            return redirect(url_for("website.index"))
        if match.home_points > match.guest_points:
            home_team.points += 3
            home_team.victories += 1
            guest_team.losses += 1
        elif match.home_points < match.guest_points:
            guest_team.points += 3
            guest_team.victories += 1
            home_team.losses += 1
        elif match.home_points == match.guest_points:
            home_team.draws += 1
            guest_team.draws += 1

