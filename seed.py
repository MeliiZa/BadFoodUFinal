"""Utility file to seed ratings database from MovieLens data in seed_data/"""

import datetime
from sqlalchemy import func

from model import User, Restaurant, Incident, connect_to_db, db
from server import app



def load_incidents(file):
    """Load ratings from u.data into database."""

    print("incident")

    for row in open(file):
        row = row.rstrip()

        user_id, upset_stomach, stomach_cramp, nausea, vomiting, diarrhea, fever, restaurant_id, date = row.split(",")

        incident = Incident(
        upset_stomach = upset_stomach,
        stomach_cramp = stomach_cramp,
        nausea = nausea,
        vomiting = vomiting,
        diarrhea = diarrhea,
        fever = fever,
        restaurant_id = restaurant_id,
        user_id = user_id,
        date = date)

        
        db.session.add(incident)


        db.session.commit()




def load_restaurant(file):
    """Load movies from u.item into database."""

    print("Restaurants")

    for row in open(file):
        row = row.rstrip()

        restaurant_name, location, zone, latitude, longitude = row.split(",")

        restaurant = Restaurant(
            restaurant_name = restaurant_name,
            location = location,
            zone = zone,
            latitude =latitude,
            longitude = longitude)

        
        db.session.add(restaurant)

        db.session.commit()



def load_users(file):
    """Load users from u.user into database."""

    print("Users")

    for row in open(file):
        row = row.rstrip()

        name, lastname, email, password = row.split(",")

        user = User(
                    name=name,
                    lastname=lastname,
                    email=email,
                    password=password)

        db.session.add(user)

        db.session.commit()        





if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    load_users("seed_data/u.users.txt")
    load_restaurant("seed_data/u.restaurants.txt")
    load_incidents("seed_data/u.incidents.txt")
    
