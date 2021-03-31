from app import app


from flask import render_template, request, redirect, url_for, flash, session
from models import *
from forms import *




@app.route("/")
def index():
    return render_template("index.html")

#REGISTRATION
@app.route("/registration", methods=['GET', 'POST'])
def registration():
    reg_form = RegForm()
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        #username exist???
        user_object = Users.query.filter_by(username = username).first()
        if user_object:
            return "Someone else has that username!"

        # add user in db
        user = Users(username = username, password = password)
        db.session.add(user)
        db.session.commit()
        return 'Now you are in db'

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