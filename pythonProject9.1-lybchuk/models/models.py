from app import db
class Plant(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    tytle = db.Column(db.String(255), nullable = False)