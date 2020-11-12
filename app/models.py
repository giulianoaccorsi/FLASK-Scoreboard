from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login


class User(UserMixin, db.Model):
    """
    Create users table
    """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    password = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"<User ID: {self.id} - User email: {self.email}>"


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Team(db.Model):
    """
    Create teams table
    """

    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), index=True, unique=True)
    acronym = db.Column(db.String(10), index=True, unique=True)
    local = db.Column(db.String(30), index=True)
    points = db.Column(db.Integer, default=0, index=True)
    victories = db.Column(db.Integer, default=0)
    draws = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Team ID: {self.id} - Team name: {self.name} - Team Acronym: {self.acronym}>"


class Match(db.Model):
    """
    Create matches table
    """

    __tablename__ = "matches"

    id = db.Column(db.Integer, primary_key=True)
    home_team = db.Column(db.String(40))
    guest_team = db.Column(db.String(40))
    home_points = db.Column(db.String(3))
    guest_points = db.Column(db.String(3))

    def __repr__(self):
        return f"<Match ID: {self.id}>"
