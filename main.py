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

if __name__ == "__main__":
    app.run(debug = True)

