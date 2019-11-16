
from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from secret import keys
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

    new_user = User( name=name, lastname=lastname, email=email, password=password)

    db.session.add(new_user)
    db.session.commit()
    db.session.refresh(new_user)

    flash(f"Email {email} added.")

    return render_template("userinfo.html", new_user = new_user)



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


@app.route('/users/<int:user_id>')
def user_info(user_id):

    user= User.query.get(user_id)

    return render_template("userinfo.html", new_user = user)



@app.route('/logout')
def logout():
    """Log out."""

    del session["user_id"]
    flash("Logged Out.")
    return redirect("/")


# @app.route('/decision', methods=['GET'])
# def decision():
#     """Lets de user decide between input a symptom or view the restaurants with incidents"""
#     return render_template("decision.html")


@app.route('/incident', methods=['GET'])
def incident_form():
    """Show login form."""
    print("get inicident")
    return render_template("incident_form.html")


@app.route('/incident', methods=['POST'])
def incident():

    user_id=session["user_id"]
    upset_stomach = request.form.get("upset_stomach")
    stomach_cramp = request.form.get("stomach_cramp")
    nausea = request.form.get("nausea")
    vomiting = request.form.get("vomiting")
    diarrhea = request.form.get("diarrhea")
    fever = request.form.get("fever")
    restaurant_id = request.form.get("restaurant_id")
    date= request.form.get("date")
    

    new_input = Incident(user_id=user_id,
                         upset_stomach=upset_stomach,
                         stomach_cramp=stomach_cramp,
                         nausea=nausea,
                         vomiting=vomiting, 
                         diarrhea=diarrhea, 
                         fever=fever, 
                         restaurant_id = restaurant_id, 
                         date= date)
     

    db.session.add(new_input)
    db.session.commit()

    flash(f"Symptoms added to your report")
    return render_template("thanks.html")

#@app.route('/moredetails', methods=['GET'])
#def moredetails():
    
#    return render_template ("thanks.html")

@app.route('/thanks', methods=['GET'])
def thanks():
    """Show thanks."""

    return render_template("thanks.html")

@app.route('/map', methods=['GET'])
def map():
    """Show thanks."""

    return render_template("map.html",google_map_api=keys['google_map_api']
)



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension

    # Do not debug for demo
    app.debug = False

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
