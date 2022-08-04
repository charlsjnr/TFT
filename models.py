from sqlalchemy import ForeignKey
from main import db
from sqlalchemy.orm import declarative_base, relationship

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

    