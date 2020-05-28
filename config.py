import os
basedir = os.path.dirname(os.path.abspath(__file__))

SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(os.path.join(basedir, "names.db"))
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False
