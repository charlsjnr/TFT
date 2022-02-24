from sqlalchemy import ForeignKey
from main import db

class Booms(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    gif = db.Column(db.Text)
    image = db.Column(db.Text)

class Champion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    synergy_id = db.Column(db.Integer, ForeignKey('Synergy.id'))
    cost_id = db.Column(db.Integer, ForeignKey('Cost.id'))

class Cost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cost = db.Column(db.Integer)

class Legends(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    rarity_id = db.Column(db.Integer, ForeignKey('Rarity.id'))
    race_id = db.Column(db.Text)
    skin_id = db.Column(db.Integer, ForeignKey('Skin.id'))

class Maps(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    image = db.Column(db.Text)

class Race(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

class Rarity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

class Skin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

class Synergy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    image = db.Column(db.Text)


    