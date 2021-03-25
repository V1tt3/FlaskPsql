from app import app
from flask import render_template



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Registration")
def registration():
    return render_template("registration.html")

