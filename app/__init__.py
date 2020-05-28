from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import model

# tworzenie aplikacji flask
app = Flask(__name__, template_folder='templates')
app.config.from_object('config')

# baza danych z SQLALCHEMY
db = SQLAlchemy(app)
migrate = Migrate(app, db)

Bootstrap(app)

# stworzenie modelu do predykcji
model_names = model.create_model(5)

# import widokow
from app import routes
