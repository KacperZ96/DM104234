from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import model


app = Flask(__name__, template_folder='templates')
app.config.from_object('config')


db = SQLAlchemy(app)
migrate = Migrate(app, db)

Bootstrap(app)


model_names = model.create_model(5)


from app import routes
