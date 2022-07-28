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

@app.route('/little_legends')
def legends():
    return render_template("legends.html")

@app.route('/synergies')
def booms():
    return render_template("synergies.html")

@app.route('/arena')
def arena():
    return render_template("arena.html")

@app.route('/login')
def login():
    return render_template("login_html")



if __name__ == "__main__":
    app.run(debug = True)

#