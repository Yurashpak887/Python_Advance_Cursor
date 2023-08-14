from models.models import *

def get_models_by_mark_id(mark_id):
    models = Modelcar.query.filter_by(mark_id=mark_id).all()
    return models

# helpers/sorting.py

def get_sorted_cars(sort_by):
    if sort_by == 'price_asc':
        cars = Car.query.order_by(Car.price.asc()).all()
    elif sort_by == 'price_desc':
        cars = Car.query.order_by(Car.price.desc()).all()
    elif sort_by == 'date_old':
        cars = Car.query.order_by(Car.year.asc()).all()
    elif sort_by == 'date_new':
        cars = Car.query.order_by(Car.year.desc()).all()
    else:
        cars = Car.query.all()
    return cars
