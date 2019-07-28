"""Utility file to seed ratings database from MovieLens data in seed_data/"""

import datetime
from sqlalchemy import func

from model import User, Restaurant, Incident, connect_to_db, db
from server import app


def load_users():
    """Load users from u.user into database."""

    print("Users")

    for i, row in enumerate(open("seed_data/u.user")):
        row = row.rstrip()
        user_id, name, lastname, email, password = row.split(",")

        user = User(user_id=user_id,
                    name=name,
                    lastname=lastname,
                    email=email,
                    password=password)

        # We need to add to the session or it won't ever be stored
        db.session.add(user)

        # provide some sense of progress
        if i % 100 == 0:
            print(i)

    # Once we're done, we should commit our work
    db.session.commit()


def load_restaurant():
    """Load movies from u.item into database."""

    print("Restaurant")

    for i, row in enumerate(open("seed_data/u.restaurants")):
        row = row.rstrip()

        # clever -- we can unpack part of the row!
        restaurant_id,restaurant_name, location, zone, latitude, longitude = row.split(",")

        # The date is in the file as daynum-month_abbreviation-year;
        # we need to convert it to an actual datetime object.

        if released_str:
            released_at = datetime.datetime.strptime(released_str, "%d-%b-%Y")
        else:
            released_at = None

        # Remove the (YEAR) from the end of the title.

        title = title[:-7]   # " (YEAR)" == 7

        movie = Movie(movie_id=movie_id,
                      title=title,
                      released_at=released_at,
                      imdb_url=imdb_url)

        # We need to add to the session or it won't ever be stored
        db.session.add(movie)

        # provide some sense of progress
        if i % 100 == 0:
            print(i)

    # Once we're done, we should commit our work
    db.session.commit()


def load_incidents():
    """Load ratings from u.data into database."""

    print("incidents")

    for i, row in enumerate(open("seed_data/u.incidents")):
        row = row.rstrip()

        incident_id,upset_Stomach,Stomach_cramps,Nausea,Vomiting,Diarrhea,
        Fever,Restaurant_ID,User_ID,Date = row.split(",")

        incident_id = incident_id
        upset_Stomach=upset_Stomach
        Stomach_cramps=Stomach_cramps
        Nausea=Nausea
        Vomiting=Vomiting
        Diarrhea=Diarrhea
        Fever=Fever
        Restaurant_ID = int(restaurant_id)
        user_id= int(user_id)
        date= date

        # We don't care about the timestamp, so we'll ignore this

        rating = Rating(user_id=user_id,
                        movie_id=movie_id,
                        score=score)

        # We need to add to the session or it won't ever be stored
        db.session.add(rating)

        # provide some sense of progress
        if i % 1000 == 0:
            print(i)

            # An optimization: if we commit after every add, the database
            # will do a lot of work committing each record. However, if we
            # wait until the end, on computers with smaller amounts of
            # memory, it might thrash around. By committing every 1,000th
            # add, we'll strike a good balance.

            db.session.commit()

    # Once we're done, we should commit our work
    db.session.commit()


def set_val_user_id():
    """Set value for the next user_id after seeding database"""

    # Get the Max user_id in the database
    result = db.session.query(func.max(User.user_id)).one()
    max_id = int(result[0])

    # Set the value for the next user_id to be max_id + 1
    query = "SELECT setval('users_user_id_seq', :new_id)"
    db.session.execute(query, {'new_id': max_id + 1})
    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    load_users()
    load_restaurant()
    load_incidents()
    set_val_user_id()
