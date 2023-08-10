from app import db


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    model = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    mileage = db.Column(db.Integer, nullable=False)
    engine = db.Column(db.Numeric(precision=5, scale=2, asdecimal=False), nullable=False)
    image_url = db.Column(db.String(255))  # Колонка для збереження URL зображення
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('cars', lazy=True))

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.Integer, nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)



class Mark(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    models = db.relationship('Modelcar', backref='mark', lazy=True)


class Modelcar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    mark_id = db.Column(db.Integer, db.ForeignKey('mark.id'), nullable=False)