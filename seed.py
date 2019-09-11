"""Utility file to seed ratings database from MovieLens data in seed_data/"""

import datetime
from sqlalchemy import func

from model import User, Restaurant, Incident, connect_to_db, db
from server import app


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

        # We need to add to the session or it won't ever be stored
        db.session.add(user)

        db.session.commit()


def load_restaurant(file):
    """Load movies from u.item into database."""

    print("Restaurant")

    for i, row in open(file):
        row = row.rstrip()

        
        restaurant_name, location, zone, latitude, longitude = row.split(",")

        restaurant = Restaurant(
            restaurant_name = restaurant_name,
            location = location,
            zone = zone,
            latitude =latitude,
            longitude = longitude)
        # The date is in the file as daynum-month_abbreviation-year;
        # we need to convert it to an actual datetime object.

        if released_str:
            released_at = datetime.datetime.strptime(released_str, "%d-%b-%Y")
        else:
            released_at = None



        # We need to add to the session or it won't ever be stored
        db.session.add(restaurant)

    # Once we're done, we should commit our work
        db.session.commit()


def load_incidents(file):
    """Load ratings from u.data into database."""

    print("incident")

    for i, row in enumerate(open(file)):
        row = row.rstrip()

        upset_stomach,stomach_cramps,nausea,vomiting,diarrhea,
        fever,restaurant_id,user_id,date = row.split(",")

        incident = incident(
        upset_stomach=upset_stomach,
        stomach_cramp=stomach_cramp,
        nausea=nausea,
        vomiting=vomiting,
        diarrhea=diarrhea,
        fever=fever,
        restaurant_id = int(restaurant_id),
        user_id= int(user_id),
        date= date)

        

        # We need to add to the session or it won't ever be stored
        db.session.add(incident)

    # Once we're done, we should commit our work
        db.session.commit()


# def set_val_user_id():
#     """Set value for the next user_id after seeding database"""

#     # Get the Max user_id in the database
#     result = db.session.query(func.max(User.user_id)).one()
#     max_id = int(result[0])

#     # Set the value for the next user_id to be max_id + 1
#     query = "SELECT setval('users_user_id_seq', :new_id)"
#     db.session.execute(query, {'new_id': max_id + 1})
#     db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    load_users("seed_data/u.users")
    load_restaurant("seed_data/u.restaurants.csv")
    load_incidents("seed_data/u.incidents.txt")
    
