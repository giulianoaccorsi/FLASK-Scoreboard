from flask import url_for, render_template, redirect, flash
from flask_login import login_required, login_user, logout_user, current_user
from . import auth
from app import db
from app.models import User
from .forms import RegistrationForm, LoginForm


@auth.route("/cadastrar", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            email = form.email.data,
            is_admin=form.admin.data
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Cadastro realizado com sucesso! Faça login a seguir.', "success")
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form, title="Cadastrar")


@auth.route("/entrar", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            login_user(user)
            if user.is_admin:
                return redirect(url_for('admin.home'))
            return redirect(url_for("website.dashboard"))
        else:
            flash("Usuário ou senha inválidos", "error")
    return render_template("auth/login.html", form=form, title="login")


@auth.route("/sair")
@login_required
def logout():
    logout_user()
    flash("Você saiu de sua conta!", "success")
    return redirect(url_for("auth.login"))
