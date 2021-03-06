"""
App.py file for Gym Rat Dictionaries:
- User authentication
- CRUD operations for definitions and categories
- Upvote and downvote functionality
- Add to favourites functionality
- Error handling
"""
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask_paginate import Pagination, get_page_args
if os.path.exists("env.py"):
    import env

# Add additional configuration to the app:
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.context_processor
def category_menu():
    """
    Injects a dictionary of the categories collection
    automatically into the context of the template, in
    this case, into the navbar dropdown menu in base.html.
    """
    categories = list(mongo.db.categories.find())
    return dict(categories=categories)


@app.route("/")
@app.route("/home")
def home():
    """
    App route for the landing page of Gym Rat Dictionaries.
    """
    return render_template("index.html")


@app.route("/get_definitions")
def get_definitions():
    """
    App route for the definitions page of Gym Rat Dictionaries.
    Displays all recently added definitions.
    """
    # Definition pagination:
    # pylint: disable=unbalanced-tuple-unpacking
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    # Reset per_page and offset values:
    per_page = 8
    offset = (page - 1) * per_page
    total = mongo.db.definitions.find().count()
    # Find definitions to display on definitions.html:
    definitions = list(mongo.db.definitions.find().sort("_id", -1))
    definitions_pagination = definitions[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page,
                            total=total, css_framework='materializecss')
    return render_template("definitions.html",
                           definitions=definitions_pagination,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    App route for search functionality.
    """
    query = request.args.get("query")
    # Pagination for returned search queries:
    # pylint: disable=unbalanced-tuple-unpacking
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    # Reset per_page and offset values:
    per_page = 8
    offset = (page - 1) * per_page
    total = mongo.db.definitions.find({"$text": {"$search": query}}).count()
    # Perform a $search on any $text index from the collection
    # using query variable:
    definitions = list(mongo.db.definitions.find(
        {"$text": {"$search": query}}))
    definitions_pagination = definitions[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page,
                            total=total,
                            css_framework='materializecss')
    return render_template("definitions.html",
                           definitions=definitions_pagination,
                           page=page, per_page=per_page,
                           pagination=pagination,)


@app.route("/category_pg/<category_id>")
def category_pg(category_id):
    """
    This function dynamically generates a page for the category
    selected by the user in the nav dropdown menu. Users can view
    definitions filtered by category.
    """
    # Pagination for definitions displayed in category_pg:
    # pylint: disable=unbalanced-tuple-unpacking
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    # Reset per_page and offset values:
    per_page = 8
    offset = (page - 1) * per_page
    # Find category by ID:
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    # Find definitions by category name:
    definitions = list(mongo.db.definitions.find(
        {"category_name": category["category_name"]}))
    total = len(definitions)
    definitions_pagination = definitions[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page,
                            total=total,
                            css_framework='materializecss')
    return render_template("category_pg.html",
                           definitions=definitions_pagination,
                           category=category,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,)


# User Authentication:

@app.route("/register", methods=["GET", "POST"])
def register():
    """
    App route for the registration functionality & page. Check to see if the
    username already exists in the database and if not, creates a dictionary
    to insert the new username and password into the db.
    """
    if "user" in session:
        flash("You are already registered and signed in!")
        return redirect(url_for('get_definitions'))

    if request.method == "POST":
        # Check if username already exists in the db:
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Sorry! This username already exists")
            return redirect(url_for("register"))

        # 'registry' is the dict that will be inserted in to the db:
        registry = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "user_favourites": []
        }
        mongo.db.users.insert_one(registry)

        # Put the new user into 'session' cookie:
        session["user"] = request.form.get("username").lower()
        flash("Registration successful!")
        return redirect(url_for("profile", user=session["user"]))

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
    # Check user is logged in:
    if "user" in session:
        # Check if the username exists in the db:
        existing_user = mongo.db.users.find_one(
            {"username": session["user"]})

        # Confirm if existing user is already logged in if not,
        # redirect to login:
        if existing_user:
            flash("You are already logged in!")
            return redirect(url_for('get_definitions'))

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
                    "profile", user=session["user"]))
            else:
                # Invalid password hash:
                flash("Incorrect Username or Password")
                return redirect(url_for("login"))

        else:
            # Username doesn't exist:
            flash("Incorrect Username or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<user>", methods=["GET", "POST"])
def profile(user):
    """
    Once logged in or registered, the profile function will be triggered
    and will redirect the session user to their profile page.
    """
    if "user" in session:
        # Grab the session user from the db:
        user = mongo.db.users.find_one(
            {"username": session["user"]})

        # If session user cookie truthy, return to appropriate profile:
        if session["user"]:
            # Render user_definitions and favourites to the profile page:
            user_definitions = list(mongo.db.definitions.find(
                {"created_by": session["user"]}
            ))
            # Create new array for definitions in user_favourites:
            new_arr = [x for x in user["user_favourites"]]
            # Find id in new array to match to correct array:
            favourites = list(mongo.db.definitions.find(
                {"_id": {"$in": new_arr}}
            ))
            return render_template("profile.html", user=user,
                                   definitions=user_definitions,
                                   user_favourites=favourites)

        # If false or doesn't exist, redirect to login:
        return redirect(url_for("login"))
    else:
        flash("You must be logged in to view your profile page!")
        return render_template("login.html")


@app.route("/logout")
def logout():
    """
    Removes user from session cookie and specifies which
    session cookie to delete. Before logging the user out,
    they will get a flash message advising that they have
    been logged out and will be redirected to login.
    """
    # Check user is logged in:
    if "user" in session:
        # Remove user from session cookie:
        flash("You have been logged out")
        session.pop("user")
        return redirect(url_for("login"))
    else:
        flash("You are not logged in yet!")
        return render_template("login.html")


# Definition CRUD operations:

@app.route("/add_definition", methods=["GET", "POST"])
def add_definition():
    """
    This functions triggers the redirect to
    add_definition.html allowing the user to
    insert a new definition to the db and redirects
    them to the home page (definitions.html)
    """
    if "user" in session:
        # POST method functionality:
        if request.method == "POST":
            definition = {
                "category_name": request.form.get("category_name"),
                "exercise_name": request.form.get("exercise_name"),
                "exercise_description": request.form.get(
                                    "exercise_description"),
                "tempo": request.form.get("tempo"),
                "imge_url": request.form.get("image_url"),
                "created_by": session["user"],
                "upvote": [],
                "downvote": []
            }
            mongo.db.definitions.insert_one(definition)
            flash("Your definition has been added successfully.")
            return redirect(url_for("get_definitions"))
        categories = list(mongo.db.categories.find().sort(
                                "category_name", 1))
        return render_template("add_definition.html",
                               categories=categories)
    else:
        flash("You must be logged in to add a definition")
        return redirect(url_for('login'))


@app.route("/edit_definition/<definition_id>", methods=["GET", "POST"])
def edit_definition(definition_id):
    """
    This function is triggered by the 'Edit'
    buttons found on all definition card panels.
    It redirects the user to the edit_definition
    form and allows them to edit a specific definition,
    updating it in the db.
    """
    if "user" in session:
        # Assign session user to variable:
        user = session["user"]

        # Find definition_id:
        definition = mongo.db.definitions.find_one(
            {"_id": ObjectId(definition_id)}
        )

        # Assign definition creator to variable:
        creator = definition["created_by"]

        # Confirm session user created this definition prior to edit:
        if user == creator:
            # POST method functionality:
            if request.method == "POST":
                submit = {
                    "category_name": request.form.get("category_name"),
                    "exercise_name": request.form.get("exercise_name"),
                    "exercise_description": request.form.get(
                                            "exercise_description"),
                    "tempo": request.form.get("tempo"),
                    "imge_url": request.form.get("image_url"),
                    "created_by": session["user"],
                    "upvote": request.form.get("upvote"),
                    "downvote": request.form.get("downvote")
                }
                mongo.db.definitions.update_one(
                    {"_id": ObjectId(definition_id)}, {"$set": submit})
                flash("Your definition has been updated successfully.")
            definition = mongo.db.definitions.find_one(
                {"_id": ObjectId(definition_id)})
            categories = list(mongo.db.categories.find().sort(
                "category_name", 1))
            return render_template("edit_definition.html",
                                   definition=definition,
                                   categories=categories)
        else:
            flash("I'm afraid you can only edit your own posts")
            return redirect(url_for('get_definitions'))
    else:
        flash("You must be logged in to edit a definition")
        return redirect(url_for('login'))


@app.route("/delete_definition/<definition_id>")
def delete_definition(definition_id):
    """
    This function is triggered by the 'Delete'
    buttons found on all definition card panels.
    When clicked, user confirmation is required
    through a modal. Once deleted the definition
    is removed from the database and the user is
    redirected to the home page.
    """
    if "user" in session:
        # Assing session user to variable:
        user = session["user"]

        # Find definition by ID:
        definition = mongo.db.definitions.find_one(
            {"_id": ObjectId(definition_id)})

        # Assing definition creator to variable:
        creator = definition["created_by"]

        # Confirm the session user is the creator of the definition
        # or a site admin:
        if user == creator or session["user"] == "admin":
            # Delete definition:
            mongo.db.definitions.remove({"_id": ObjectId(definition_id)})
            flash("Definition successfully deleted.")
            return redirect(url_for("get_definitions"))
        else:
            flash("I'm afraid you cannot delete another users post")
            return render_template("definitions.html")
    else:
        flash("You must be logged in to delete a post")
        return redirect(url_for('login'))


# Additional site functionality/features:

@app.route("/upvote/<definition_id>", methods=["GET", "POST"])
def upvote(definition_id):
    """
    This function will add the user_id to the upvote
    array in the definitions collection and
    display the length of the array on the upvote icon.
    """
    if "user" in session:
        # Grab user from the database:
        user = mongo.db.users.find_one(
            {"username": session["user"]})

        # Grab definition from the db using the definition ID:
        definition = mongo.db.definitions.find_one(
            {"_id": ObjectId(definition_id)}
        )

        # Check if user has already downvoted the same definition:
        if user["_id"] in definition["downvote"]:
            flash("You've already downvoted this definition")
            return redirect(url_for('get_definitions'))
        # Check if user has already upvoted the definition and pull
        # user ID from upvote array:
        elif user["_id"] in definition["upvote"]:
            mongo.db.definitions.find_one_and_update(
                {"_id": ObjectId(definition_id)},
                {"$pull": {"upvote": user["_id"]}}
            )
            flash("Your upvote on this definition has been removed")
            return redirect(url_for('get_definitions'))
        else:
            # Find definition by ID and update the upvote array with the
            # user ID:
            mongo.db.definitions.find_one_and_update(
                {"_id": ObjectId(definition_id)},
                {"$addToSet": {"upvote": user["_id"]}},
                {"upsert": "true"}
            )

            return redirect(url_for('get_definitions'))
    else:
        flash("You must be logged in to upvote a definition")
        return redirect(url_for('login'))


@app.route("/downvote/<definition_id>")
def downvote(definition_id):
    """
    This function will add the user_id to the downvote
    array in the definitions collection and display
    the length of the array on the downvote icon.
    """
    if "user" in session:
        # Grab user from the database:
        user = mongo.db.users.find_one(
            {"username": session["user"]})

        # Grab definition from the db using the definition ID:
        definition = mongo.db.definitions.find_one(
            {"_id": ObjectId(definition_id)}
        )

        # Check if user has already upvoted this definition_id:
        if user["_id"] in definition["upvote"]:
            flash("You've already upvoted this definition")
            return redirect(url_for('get_definitions'))
        # Check if user has already downvoted this definition
        # and pull user ID from downvote array:
        elif user["_id"] in definition["downvote"]:
            mongo.db.definitions.find_one_and_update(
                {"_id": ObjectId(definition_id)},
                {"$pull": {"upvote": user["_id"]}}
            )
            flash("Your downvote on this definition has been removed")
            return redirect(url_for('get_definitions'))
        else:
            mongo.db.definitions.find_one_and_update(
                {"_id": ObjectId(definition_id)},
                {"$addToSet": {"downvote": user["_id"]}},
                {"upsert": "true"}
            )

            return redirect(url_for('get_definitions'))
    else:
        flash("You must be logged in to downvote a definition")
        return redirect(url_for('login'))


@app.route("/get_definitions/<definition_id>")
def add_to_favourites(definition_id):
    """
    This function adds definitions into users
    'favourites', an array stored in each user document.
    These definitions can then be viewed on their
    profile page.
    """
    # Check user is logged in:
    if "user" in session:
        # Grab the session user from the db:
        user = mongo.db.users.find_one(
            {"username": session["user"]})

        # Check if definition_id is already in user_favourites array:
        if ObjectId(definition_id) in user["user_favourites"]:
            flash("You've already added this definition to your favourites")
            return redirect(url_for('get_definitions'))

        # Insert definition_id into user_favourites array:
        mongo.db.users.find_one_and_update(
            {"username": user["username"]},
            {"$addToSet":
                {"user_favourites": ObjectId(definition_id)}}
        )
        flash("Saved to your favourites")
        return redirect(url_for('get_definitions'))
    else:
        flash("You must be logged in to save a definition to your favourites")
        return redirect(url_for('login'))


# Category CRUD operations:
@app.route("/get_categories")
def get_categories():
    """
    App route for categories.html, which
    displays categories to admin users from
    which they can perform CRUD operations to.
    """
    # Confirm user is logged in, else, redirect to login:
    if "user" in session:

        # Confirm session user is an admin else redirect:
        if session["user"] == "admin":
            categories = list(mongo.db.categories.find().sort(
                "category_name", 1))
            return render_template("categories.html",
                                   categories=categories,
                                   user=session["user"])
        else:
            flash("Whoops!")
            return render_template("403.html")
    else:
        flash("You must be logged in to view this page")
        return redirect(url_for('login'))


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """
    This function inserts a new category into the
    database, using the data from the add_category form.
    """
    # Confirm user is logged in, else redirect to login:
    if "user" in session:

        # Confirm session user is an admin else redirect:
        if session["user"] == "admin":
            if request.method == "POST":
                category = {
                    "category_name": request.form.get("category_name")
                }
                mongo.db.categories.insert_one(category)
                flash("New Category Successfully Added")
                return redirect(url_for("get_categories"))

            return render_template("add_category.html")
        else:
            flash("Whoops!")
            return render_template("403.html")
    else:
        flash("You must be logged in to view this page")
        return redirect(url_for('login'))


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    """
    This function edits a specific category
    already stored in the database. Admins update
    the existing data provided in the edit_category
    form and update the category in the database.
    """
    # Confirm user is logged in else, redirect to login:
    if "user" in session:

        # Confirm session user is an admin else redirect:
        if session["user"] == "admin":
            if request.method == "POST":
                # Insert dictionary into database:
                submit = {
                    "category_name": request.form.get("category_name")
                }
                mongo.db.categories.update(
                    {"_id": ObjectId(category_id)}, submit)
                flash("Category Update Successful")
                return redirect(url_for("get_categories"))

            category = mongo.db.categories.find_one(
                    {"_id": ObjectId(category_id)})
            return render_template("edit_category.html",
                                   category=category)
        else:
            flash("Whoops!")
            return render_template("403.html")
    else:
        flash("You must be logged in to view this page")
        return redirect(url_for('login'))


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    """
    This function deletes a specific category
    from the database. Triggered by the 'Delete'
    button, when clicked, user confirmation is required
    through a modal.
    """
    # Confirm user is logged in else, redirect to login:
    if "user" in session:

        # Confirm session user is an admin else redirect:
        if session["user"] == "admin":
            mongo.db.categories.remove(
                {"_id": ObjectId(category_id)})
            flash("Category Successfully Deleted")
            return redirect(url_for("get_categories"))
        else:
            flash("Whoops!")
            return render_template("403.html")
    else:
        flash("You must be logged in to view this page")
        return redirect(url_for('login'))


# Error handlers custom pages
# https://flask.palletsprojects.com/en/2.0.x/errorhandling/#custom-error-pages

@app.errorhandler(403)
def forbidden(e):
    """
    403 Forbidden client error status
    response code custom HTML page.
    """
    return render_template('403.html'), 403


@app.errorhandler(404)
def page_not_found(e):
    """
    404 page not found error status
    response code custom HTML page.
    """
    return render_template('404.html'), 404


@app.errorhandler(500)
def generic(e):
    """
    500 Internal server error status
    response code custom HTML page.
    """
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
