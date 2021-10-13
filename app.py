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

"""
App route for the landing page of Gym Rat Dictionaries. 
"""
@app.route("/")
@app.route("/get_definitions")
def get_definitions():
    definitions = mongo.db.definitions.find()
    return render_template("definitions.html", definitions=definitions)

"""
App route for the registration functionality and page.
"""
@app.route("/register", methods=["GET", "POST"])
def register():
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
        mongo.db.insert_one(register)

        # Put the new user into 'session' cookie:
        session["user"] = request.form.get("username").lower()
        flash("Registration successful!")
    return render_template("register.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
