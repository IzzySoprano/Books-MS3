import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)


app = Flask(__name__)


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        print("Testing registration site")
    return render_template("register.html")

if __name__== "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True) # debug should be = false when submitting. Only true when testing your application
        