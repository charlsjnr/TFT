#imports Flask to activate website
from flask import Flask, render_template

app = Flask(__name__)

#creates route for home page
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/directory')
def directory():
    return render_template("directory.html")

@app.route('/champions')
def champions():
    return render_template("champions.html")

@app.route('/little_legends')
def legends():
    return render_template("legends.html")

@app.route('/booms')
def booms():
    return render_template("booms.html")

@app.route('/arena')
def arena():
    return render_template("arena.html")

@app.route('/login')
def login():
    return render_template("login_html")



if __name__ == "__main__":
    app.run(debug = True)

#