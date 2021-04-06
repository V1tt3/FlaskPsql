from flask import Flask, render_template
from config import Configurations 

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager



app = Flask(__name__)

app.config.from_object(Configurations)

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.init_app(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)





