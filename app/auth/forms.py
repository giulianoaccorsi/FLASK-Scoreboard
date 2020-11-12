from flask_wtf import FlaskForm
from wtforms import (
    PasswordField,
    StringField,
    SubmitField,
    ValidationError,
    BooleanField
)
from wtforms.validators import DataRequired, Email, EqualTo
from app.models import User


class RegistrationForm(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Senha", validators=[DataRequired(), EqualTo("confirm", message="As senhas não coincidem!")])
    confirm = PasswordField("Confirme a senha")
    admin = BooleanField("Admin ?")
    submit = SubmitField("Cadastrar")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email já utilizado! Escolha outro.")


class LoginForm(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("Login")