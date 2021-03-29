from flask import Flask, render_template
from config import Configurations 

from flask_sqlalchemy import SQLAlchemy
from flask_login import login_manager
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager



app = Flask(__name__)

app.config.from_object(Configurations)

db = SQLAlchemy(app)

#log_manager = login_manager(app)


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)





