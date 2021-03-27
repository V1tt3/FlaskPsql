
from app import app
from flask import render_template, request, redirect, url_for, flash, session
from models import Users




@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Registration")
def registration():
    return render_template("registration.html")

@app.rote("/login", methods = ['GET, POST'])
def login_page():
    login = request.form.get('login')
    password = request.form.get('password')

    if login and password:
        if login in Users.username:
            
    else:
        return render_template('login.html')
    

@app.route("/logout", methods = ['GET, POST'])
def logout():
    pass