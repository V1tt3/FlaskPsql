from flask import Flask, render_template
from config import Configurations 
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_manager


app = Flask(__name__)

app.config.from_object(Configurations)

db = SQLAlchemy(app)

manager = login_manager(app)





