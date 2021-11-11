import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
     import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check to see if username exists within the database
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user:
                flash("email already exists")
                return redirect(url_for("register"))

        register =  {
            "email": request.form.get("email").lower(),
            "password": request.form.get("password")
        }
        mongo.db.users.insert_one(register)

        # Put the session user into a sesion cookie 
        session["user"] = request.form.get("email").lower
        flash("Registration successful")
    return render_template("register.html")


    
if __name__== "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True) # debug should be = false when submitting. Only true when testing your application
        