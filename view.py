from app import app, login_manager


from flask import render_template, request, redirect, url_for, flash, session
from flask_login import login_user, logout_user, current_user, login_required
from models import *
from forms import *


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)

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

        username = log_form.username.data
        user = Users.query.filter_by(username = username).first()
        login_user(user)
        if current_user.is_authenticated:
            return ('Success!!, now you are logged in')
        else:
            return ('Not logged in')

    return render_template("login.html", form = log_form)
    

@app.route("/logout", methods = ['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))