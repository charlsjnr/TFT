#imports Flask to activate website
from distutils.log import debug
from flask import Flask, render_template, redirect, abort, flash, url_for, request
from flask_login import LoginManager, logout_user, login_user, current_user, login_required
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from forms import LoginForm, RegisterForm
import models

app = Flask(__name__)

app.config['SECRET_KEY'] = "sus"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
login_manager = LoginManager(app)
login_manager.init_app = 'login'

db = SQLAlchemy(app)

@login_manager.user_loader
def load_user(id):
    return models.User.query.get(int(id))

#creates route for home page
@app.route('/')
def home():
    return render_template("home.html")

#creates route to show champions
@app.route('/champions')
def champions():
    #query to get everything from champions table
    champions = models.Champion.query.all()
    return render_template("champions.html", champions=champions)



#creates route for a champion from champions page
@app.route('/champions/<string:id>')
def championid(id):
    #query to get champion where id = id
    champions = models.Champion.query.filter_by(id=id).first()
    if current_user.is_authenticated:
        user = models.User.query.filter_by(id=current_user.id).first()
    else:
        user = None
    return render_template("championid.html", champions=champions, user=user)


#creates route to show favourites
@app.route('/favourites')
def favourites():
    #query to get everything from champions table
    user = models.User.query.filter_by(id=current_user.id).first_or_404()
    return render_template("favourites.html", user=user)
    
# Route to add champions to favourites table
@app.route("/favourite/<int:id>", methods=["GET", "POST"])
@login_required  # requires user to be logged in to add favourite
def favourite(id):
    # Adds favourite champions by assigining current user id to user id table
    # and adds the champion id to champions id table.
    user = models.User.query.filter_by(id=current_user.id).first_or_404()
    champion = models.Champion.query.filter_by(id=id).first_or_404()
    user.champions.append(champion)
    db.session.merge(user)
    db.session.commit()
    flash ("Champion added to favourites")
    return redirect(url_for("championid", id=champion.id))

# route to remove a champion from your favourites
@app.route("/delete/<int:id>", methods=["GET", "POST"])
@login_required
def delete(id):
    user = models.User.query.filter_by(id=current_user.id).first_or_404()
    champion = models.Champion.query.filter_by(id=id).first_or_404()
    user.champions.remove(champion)
    db.session.merge(user)
    db.session.commit()
    flash ("Champion removed to favourites")
    return redirect(url_for("championid", id=champion.id))

#creates route for synergies
@app.route('/synergies')
def synergies():
    #query to get everything from synergies
    synergies = models.Synergy.query.all()
    return render_template("synergies.html", synergies=synergies)

#creates route got a synergy in synergies page
@app.route('/synergies/<string:id>')
def synergiesid(id):
    #query to get synergy where id = id
    synergies = models.Synergy.query.filter_by(id=id).first()
    return render_template("synergyid.html", synergies=synergies)

@app.route('/profile/<int:id>')
@login_required #requires user to be logged in before viewing their profile
def profile(id):
    if current_user.no_login:
        flash('Please log in before viewing your profile')
        return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
        # if user is already logged in it redirects them home
    form = LoginForm()
    if form.validate_on_submit():
        user = models.User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Incorrect email address or password.')
            # queries DB if user input email and password is correct and
            # if not it will show a message saying it was Incorrect
        else:
            login_user(user, remember=form.remember_me.data)
            flash('Logged in successfully.')
        # if user had inputted their correct information it logged them in
        next = request.args.get('next')
        return redirect(next or url_for('login'))
    return render_template('login.html', form=form, title="Login")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
        # if user is already logged in it redirects them home
    form = RegisterForm()
    if form.validate_on_submit():

        existing_email = models.User.query.filter_by(email=form.email.data).first()
        if existing_email is not None: #  checks if email is already registered
            print("this is what's up")

            flash ("Email already registered.", 'user')

            return redirect('register')
            # if user's email is already used it redirects them back to the
            # register page and shows them a message saying the email is
            # already being used
        else:
            user = models.User(email=form.email.data)
            user.set_password(form.password.data)
            print(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('You are now a registered user.')
            print("this is what's up2")
            return redirect(url_for('login'))
        # if the email inteded to use during register is available
        # the email will be put in to the DB and password will be hashed
        # then also put in the DB
    return render_template("register.html", form=form, title="Register")

@app.route("/logout")
@login_required
def logout():
    # uses flask's built-in logout feature and sends user's home after
    # logging out
    logout_user()
    return redirect(url_for('home'))

@app.errorhandler(404)
def error404(error):
    return render_template('404.html', title='Error'), 404

@app.errorhandler(500)
def error500(error):
    return render_template("500.html")

@app.errorhandler(401)
def error401(error):
    return render_template("401.html")

if __name__ == "__main__":
    app.run(debug = True)
