from app import app


from flask import render_template, request, redirect, url_for, flash, session
from models import *
from forms import *




@app.route("/")
def index():
    return render_template("index.html")

#------------------------------------REGISTRATION-----------------------------------------
@app.route("/registration", methods=['GET', 'POST'])
def registration():

    reg_form = RegForm()

    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        user = Users(username = username, password = password)
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('login'))

    return render_template("registration.html", form = reg_form)

#--------------------------------------LOGIN----------------------------------------------
@app.route("/login", methods = ['GET', 'POST'])
def login():
    log_form = LogForm()
    
    if log_form.validate_on_submit():
        return "Logged in!"

    return render_template("login.html", form = log_form)
    

@app.route("/logout", methods = ['GET, POST'])
def logout():
    pass