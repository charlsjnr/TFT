#imports Flask to activate website
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import models

app = Flask(__name__)

app.config['SECRET_KEY'] = "sus"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

#creates route for home page
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/directory')
def directory():
    return render_template("directory.html")

@app.route('/champions')
def champions():
    champions = models.Champion.query.all()
    return render_template("champions.html", champions=champions)

@app.route('/champions/<string:id>')
def championid(id):
    champions = models.Champion.query.filter_by(id=id).first()
    return render_template("championid.html", champions=champions)

@app.route('/items')
def legends():
    return render_template("legends.html")

@app.route('/synergies')
def synergies():
    synergies = models.Synergy.query.all()
    return render_template("synergies.html", synergies=synergies)

@app.route('/arena')
def arena():
    return render_template("arena.html")

@app.route('/login')
def login():
    return render_template("login_html")



if __name__ == "__main__":
    app.run(debug = True)

#