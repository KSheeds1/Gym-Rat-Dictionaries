import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_definitions")
def get_definitions():
    """
    App route for the landing page of Gym Rat Dictionaries.
    Displays all recently added definitions. 
    """
    definitions = mongo.db.definitions.find()
    return render_template("definitions.html", definitions=definitions)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    App route for the registration functionality & page. Check to see if the 
    username already exists in the database and if not, creates a dictionary
    to insert the new username and password into the db. 
    """
    if request.method == "POST":
        # Check if username already exists in the db:
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Sorry! This username already exists")
            return redirect(url_for("register"))

        # 'register' is the dict that will be inserted in to the db:
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # Put the new user into 'session' cookie:
        session["user"] = request.form.get("username").lower()
        flash("Registration successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    App log-in functionality. Defensively programmed to check
    the existence of username in the db, whether the hashed 
    password matches user input. Will either log user into session 
    cookie or redirect back to login depending on whether the 
    correct username and password are provided.
    """
    if request.method == "POST":
        # Check if the username exists in the db:
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Ensure the hashed password matches user input: 
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # Invalid password hash:
                flash("Incorrect Username or Password")
                return redirect(url_for("login"))

        else:
            # Username doesn't exist:
            flash("Incorrect Username or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    Once logged in or registered, the profile function will be triggered
    and will redirect the session user to their profile page. 
    """
    # Grab the session user's username from the db:
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    # If session user cookie truthy, return to appropriate profile:
    if session["user"]:
        return render_template("profile.html", username=username)

    # If false or doesn't exist, redirect to login:
    return redirect(url_for("login"))
    

@app.route("/logout")
def logout():
    """
    Removes user from session cookie and specifies which
    session cookie to delete. Before logging the user out,
    they will get a flash message advising that they have
    been logged out and will be redirected to login. 
    """
    # Remove user from session cookie:
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
