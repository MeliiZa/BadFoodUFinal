"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the PostgreSQL database; we're getting
# this through the Flask-SQLAlchemy helper library. On this, we can
# find the `session` object, where we do most of our interactions
# (like committing, etc.)

db = SQLAlchemy()


#####################################################################
# Model definitions

class User(db.Model):
    """User of ratings website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)

    name = db.Column(db.String(64), nullable=False)
    lastname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(16), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<User user_id={self.user_id} email={self.email}>"




class Restaurant(db.Model):
    """Rating of a movie by a user."""

    __tablename__ = "restaurants"

    restaurant_id = db.Column(db.Integer,
                          autoincrement=True,
                          primary_key=True)
    restaurant_name = db.Column(db.String(2000))
    location= db.Column(db.String(4000))
    zone= db.Column(db.String(4000))
    latitude = db.Column(db.String(4000))
    longitude = db.Column(db.String(4000))
    

    # def __repr__(self):
    #     """Provide helpful representation when printed."""

    #     return f"""<Restaurant restaurant_id={self.restaurant_id} 
    #                restaurant_id={self.restaurant_id} 
    #                restaurant_name={self.restaurant_name} 
    #                location={self.location}>"""

class Incident(db.Model):

    __tablename__ = "incidents"
    
    incident_id = db.Column(db.Integer,autoincrement=True, primary_key=True,)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    upset_stomach = db.Column(db.String(30))
    stomach_cramp = db.Column(db.String(30))
    nausea = db.Column(db.String(30))
    vomiting = db.Column(db.String(30))
    diarrhea = db.Column(db.String(30))
    fever = db.Column(db.String(30))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.restaurant_id'))
    date = db.Column(db.DateTime)


#####################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///badfoodu'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will
    # leave you in a state of being able to work with the database
    # directly.
    from server import app
    connect_to_db(app)
    print("Connected to DB.")