from sqlalchemy import ForeignKey
from main import db
from sqlalchemy.orm import declarative_base, relationship
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

ChampionSynergy = db.Table('ChampionSynergy', db.Model.metadata,
    db.Column('cid', db.Integer, db.ForeignKey('Champion.id')),
    db.Column('sid', db.Integer, db.ForeignKey('Synergy.id')))

class Champion(db.Model):
    __tablename__ = 'Champion'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    cost = db.Column(db.Integer)
    img = db.Column(db.Text)


    synergies = db.relationship('Synergy', secondary=ChampionSynergy, back_populates='champions')

class Synergy(db.Model):
    __tablename__ = 'Synergy'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    image = db.Column(db.Text)

    champions = db.relationship('Champion', secondary=ChampionSynergy, back_populates='synergies')

class User(db.Model, UserMixin):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.Text, unique=True)
    password_hash = db.Column(db.Text, nullable=False)
    
    def set_password(self, password_hash):
        self.password_hash = generate_password_hash(password_hash)

    def check_password(self, password_hash):
        return check_password_hash(self.password_hash, password_hash)

    def __repr__(self):
        return '<User{}>'.format(self.email)