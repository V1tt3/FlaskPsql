from flask import Flask, render_template
from config import Configurations 

app = Flask(__name__)

app.config.from_object(Configurations)





