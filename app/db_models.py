from app import db

# Model bazy Danych
class Name(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, nullable=False)
    gender_predict = db.Column(db.String(64), index=True, nullable=False, default="N/D")
    correct = db.Column(db.String(64), index=True, nullable=False, default="N/D")
