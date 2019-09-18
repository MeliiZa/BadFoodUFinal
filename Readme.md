# <img src="/static/images/BFUheader.png">

BadFoodU is a web-based platform that uses crowdsourced data to pinpoint potential sources of food poisoning, and help people avoid getting sick. Users can enter symptoms and information about their most recent restaurant meals, and a map populates with restaurants that users have entered.

## Table of Contents🍔

* [Tech Stack](#tech-stack)
* [Features](#features)
* [Setup/Installation](#installation)
* [To-Do](#future)

## <a name="tech-stack"></a>Tech Stack

__Frontend:__ HTML, CSS (Flexbox), Javascript, jQuery, Bootstrap <br/>
__Backend:__ Python, Flask, PostgreSQL, SQLAlchemy <br/>
__APIs:__ Yelp, Google Maps <br/>

## <a name="features"></a>Features 📽

Although Registration is not required, we would love for you to create an account!

![Register](/static/images/gifs/Registration.gif)

<br/><br/><br/>
Congrats! Now you can log in.

![LogIn](/static/images/gifs/Login.gif)

<br/><br/><br/>
The fun part, enter all the symptoms you are experiencing and let us know where are the last 3 restaurants you dine out.

![Symptoms](/static/images/gifs/Symptoms.gif)

<br/><br/><br/>
Thanks for helping the community! You can know see a map with all the places people could have gone sick.

![Map](/static/images/gifs/Map.gif)

<br/><br/><br/>

## <a name="installation"></a>Setup/Installation ⌨️

#### Requirements:

- PostgreSQL
- Python 3
- Google Maps API keys

To have this app running on your local computer, please follow the below steps:

Clone repository:
```
$ git clone https://github.com/MeliiZa/BadFoodUFinal.git
```
Create a virtual environment🔮:
```
$ virtualenv env
```
Activate the virtual environment:
```
$ source env/bin/activate
```
Install dependencies🔗:
```
$ pip install -r requirements.txt
```

Get your own secret keys🔑 for Google Maps
Save them to a file `secrets.py`. Your file should look something like this:
```
keys = {'google_map_api': "XYX"}
```
Create database 'users'.
```
$ createdb users
```
Create your database restaurants and seed🌱 example data.
```
$ python3 model.py
```
Run the app from the command line.
```
$ python3 server.py
```
If you want to use SQLAlchemy to query the database, run in interactive mode
```
$ python3 -i model.py
```

## <a name="future"></a>TODO✨
* 🍔 Add ability for users to search for specific restaurants
* 🍔 Add history for users
* 🍔 Show labels on Google Maps markers that show number of ocurrences
* 🍔 Add page of Top Restaurants with ocurrences added
* 🍔 Add page so users can send us suggestions
