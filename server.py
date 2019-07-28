"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, Restaurant, Incident


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")


@app.route('/register', methods=['GET'])
def register_form():
    """Show form for user signup."""

    return render_template("register_form.html")


@app.route('/register', methods=['POST'])
def register_process():
    """Process registration."""

    # Get form variables
    name = request.form.get("name")
    lastname = request.form.get("lastname")
    email = request.form.get("email")
    password = request.form.get("password")

  


    new_user = User(name=name, lastname=lastname, email=email, password=password)

    db.session.add(new_user)
    db.session.commit()

    flash(f"User {email} added.")
    return redirect(f"/users/{new_user.user_id}")


@app.route('/login', methods=['GET'])
def login_form():
    """Show login form."""

    return render_template("login_form.html")


@app.route('/login', methods=['POST'])
def login_process():
    """Process login."""

    # Get form variables
    email = request.form.get("email")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()

    if not user:
        flash("No such user")
        return redirect("/login")

    if user.password != password:
        flash("Incorrect password")
        return redirect("/login")

    session["user_id"] = user.user_id

    flash("Logged in")
    return redirect(f"/users/{user.user_id}")


# @app.route('/logout')
# def logout():
#     """Log out."""

#     del session["user_id"]
#     flash("Logged Out.")
#     return redirect("/")


# @app.route('/decision', methods=['GET'])
# def decision():
#     """Lets de user decide between input a symptom or view the restaurants with incidents"""
#     return render_template("decision.html")


# @app.route('/incident', methods=['GET'])
# def incident_form():
#     """Show login form."""

#     return render_template("incident_form.html")


@app.route('/incident', methods=['GET','POST'])
def incident_form():

    """Process registration."""
    if flask.request.method == "GET":
        return render_template("incident_form.html")
    else:    
    # Get form variables
        upset_stomach = incident.form["upset_stomach"]
        stomach_cramps = incident.form["stomach_cramps"]
        nausea = incident.form["nausea"]
        vomiting = incident.form["vomiting"]
        diarrhea = incident.form["diarrhea"]
        fever = incident.form["fever"]

        new_input = Incident(upset_stomach=upset_stomach,stomach_cramps=stomach_cramps, nausea=nausea,vomiting=vomiting, diarrhea=diarrhea, fever=fever )

        db.session.add(incident)
        db.session.commit()

        flash(f"Symptoms added to your report")
    return redirect(f"/moredetails")

@app.route('/moredetails', methods=['GET'])
def moredetails():
    
    return render_template ("moredetails_form.html")



# @app.route('/login', methods=['GET'])
# def login_form():
#     """Show login form."""

#     return render_template("login_form.html")    
# ###@app.route("/users")
# ###def user_list():
#     """Show list of users."""

# ###    users = User.query.all()
# ###    return render_template("user_list.html", users=users)


# ###@app.route("/users/<int:user_id>")
# ###def user_detail(user_id):
#     """Show info about user."""

# ###    user = User.query.options(db.joinedload('ratings').joinedload('movie')).get(user_id)
# ###    return render_template("user.html", user=user)


# @app.route("/restaurants")
# def movie_list():
#     """Show list of movies."""

    # restaurants = restaurants.query.order_by('restaurants_name').all()
    # return render_template("restaurants_list.html", restaurants_name=restaurants_name)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension

    # Do not debug for demo
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
