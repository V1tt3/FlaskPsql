from wtforms import Form, StringField, PasswordField, validators, SubmitField, ValidationError
from flask_wtf import FlaskForm

from models import Users


def invalid_credentials(form, field):
    username_ent = form.username.data
    password_ent = field.data

    user_object = Users.query.filter_by(username = username_ent).first()
    if user_object is None:
        raise ValidationError("Username or password incorrect!")
    elif password_ent != user_object.password:
        raise ValidationError("Username or password incorrect!")

    

class RegForm(FlaskForm):
    #registration form-------------------------------------

    username = StringField('username', 
        [validators.InputRequired(), validators.Length(min=3, max=25, message='Username must be between 3 and 25 characters long')])
    password = PasswordField('password',
        [validators.InputRequired(), validators.Length(min=4, message='Minimal password length is 4 characters'), validators.EqualTo('confirm', message='Passwords don\'t match')])
    confirm = PasswordField('repeat password')
    submit_button = SubmitField('Create')

    def validate_username(self, username):
        user_object = Users.query.filter_by(username = username.data).first()
        if user_object:
            raise ValidationError("Someone has already taken this nickname, change it!")

class LogForm(FlaskForm):
    #login form-------------------------------------------

    username = StringField('username', [validators.InputRequired(message = "Username required")])
    password = PasswordField('password', [validators.InputRequired(message = "Password required"), invalid_credentials])
    submit_button = SubmitField('Login')