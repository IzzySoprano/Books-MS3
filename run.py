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

# Home page
@app.route("/")
@app.route("/home", methods=["GET", "POST"])
def home():
    all_of_the_books_in_the_collection = mongo.db.books.find()
    return render_template("home.html", books_variable=all_of_the_books_in_the_collection)


# User Registration
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check to see if password exists within the database
        existing_user = mongo.db.users.find_one(
            {"users": request.form.get("email").lower()})

        if existing_user:
            flash("email already exists")
            return redirect(url_for("register"))

        register = {
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # Put the session user into a session cookie
        session["user"] = request.form.get("email").lower()
        flash("Registration successful")
        return redirect(url_for("account", email=session["user"]))

    return render_template("register.html")


# Login Page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if Email exists
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        # print(existing_user)
        if existing_user:
            # Ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("email").lower()
                flash("Welcome, {}" .format(request.form.get("email")))
                return redirect(url_for(
                    "account", email=session["user"]))
            else:
                # Invalid password match
                flash("Incorrect Password")
                session["user"] = None
                return redirect(url_for("login"))
        else:
            # Email doesn't exist
            flash("Email doesn't exist")
            session["user"] = None
            return redirect(url_for("login"))

    return render_template("login.html")


# Account page
@app.route("/account/<email>", methods=["GET", "POST"])
def account(email):
    # Grab the user's email from db
    email = mongo.db.users.find_one(
        {"email": session["user"]})

    if session["user"]:
        return render_template("account.html", email=email)

    return render_template("login.html")


# User Logging Out
@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been Logged Out")
    session.clear()
    return redirect(url_for("home"))


# Delete book functionality
@app.route("/delete_book/<specific_bookid>",  methods=["GET", "POST"])
def delete(specific_bookid):
    book = mongo.db.books.find_one({'_id': ObjectId(specific_bookid)})
    if session.get("user"):
         book = mongo.db.books.find_one_and_delete({'_id': ObjectId(specific_bookid)})
    return render_template("home.html", book=book)


# Add Book to database
@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    # checks if user is logged in
    if session.get("user"):
        if request.method == "POST":
            # purchase link auto-generated
            purchase_link = (
                "https://www.amazon.co.uk/s?k=" +
                request.form.get("book_title")
            )
            # retrieve book info from form
            book = {
                "book_title": request.form.get("book_title"),
                "author": request.form.get("author"),
                "genre": request.form.get("genres"),
                "release_year": request.form.get("release_year"),
                "image_url": request.form.get("image_url"),
                "rating": request.form.get("rating"),
                "book_review": request.form.get("book_review"),
                "purchase_link": purchase_link,
                "created_by": session["user"],
            }
            # insert new book into db
            mongo.db.books.insert_one(book)
            flash("Book Review Added!")
            return redirect(url_for("home"))
        genres = mongo.db.genres.find().sort("genre_name", 1)
        return render_template("add_book.html", genres=genres)
    # if user is not logged in
    else:
        flash("You need to be logged in to perform this action")
        return redirect(url_for("login"))


# Edit Book Review
@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    genres = mongo.db.genres.find().sort("genre_name", 1)
    return render_template("edit_book.html", book=book, genres=genres)


# Saving edited book review
@app.route("/save_book/<book_id>", methods=["GET", "POST"])
def save_book(book_id):
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    genres = mongo.db.genres.find().sort("genre_name", 1)

    if session["user"]:
            existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

    else:
                flash(
                    "Sorry, you are not allowed to edit that!")
                return redirect(url_for('home', book_id=book["_id"]))

    mongo.db.books.update_many({"_id": ObjectId(book_id)}, {"$set": {
        "book_title": request.form.get("book_title"),
        "author": request.form.get("author"),
        "genre": request.form.get("genres"),
        "release_year": request.form.get("release_year"),
        "image_url": request.form.get("image_url"),
        "rating": request.form.get("rating"),
        "book_review": request.form.get("book_review"),
    }}, upsert=True)
    return redirect(url_for("home"))




if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)  # debug should be = false when submitting. Only true when testing your application