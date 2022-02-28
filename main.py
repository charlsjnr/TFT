#imports Flask to activate website
from flask import Flask, render_template

app = Flask(__name__)

#creates route for home page
@app.route('/')
def home():
    return render_template("home.html")



if __name__ == "__main__":
    app.run(debug = True)
