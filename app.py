from flask import Flask, render_template
from config import Configurations 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(Configurations)

db = SQLAlchemy(app)



