
from app import app
from flask import render_template, request, redirect, url_for, flash, session
from models import Users
from forms import *




@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registration", methods=['GET', 'POST'])
def registration():
    reg_form = RegForm()
    if reg_form.validate():
        return "great"

    return render_template("registration.html", form = reg_form)

@app.route("/login", methods = ['GET, POST'])
def login_page():
    #login = request.form.get('login')
    #password = request.form.get('password')

    #if login and password:
     #   if login in Users.username:
            
   # else:
    return render_template('login.html')
    

@app.route("/logout", methods = ['GET, POST'])
def logout():
    pass