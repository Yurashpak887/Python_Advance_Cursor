from models.models import *
from datetime import datetime, timedelta


def get_models_by_mark_id(mark_id):
    models = Modelcar.query.filter_by(mark_id=mark_id).all()
    return models

# helpers/sorting.py


def get_сars(selected_mark=None, selected_model_id=None, selected_year_from=None, selected_year_to=None):
    query = Car.query

    if selected_mark is not None:
        query = query.filter_by(name=selected_mark)
    if selected_model_id and selected_model_id is not None:
        query = query.filter_by(model=selected_model_id)

    if selected_year_from:
        query = query.filter(Car.year >= selected_year_from)

    if selected_year_to:
        query = query.filter(Car.year <= selected_year_to)


    return query.all()



def get_sorted_cars(sort_by, cars_list):
    if sort_by == 'price_asc':
        cars = sorted(cars_list, key=lambda car: car.price)
    elif sort_by == 'price_desc':
        cars = sorted(cars_list, key=lambda car: car.price, reverse=True)
    elif sort_by == 'date_old':
        cars = sorted(cars_list, key=lambda car: car.year)
    elif sort_by == 'date_new':
        cars = sorted(cars_list, key=lambda car: car.year, reverse=True)
    else:
        cars = cars_list

    return cars





def get_models_data(mark_id):
    mark = Mark.query.get(mark_id)
    models = [{'id': model.id, 'name': model.name} for model in mark.models]
    return models


def count_of_all_car(selected_cars=None):
    if selected_cars is None:
        selected_cars = Car.query.all()
    carlist = len(selected_cars)
    return carlist


def count_of_cars_last_day(selected_cars=None):
    today = datetime.now()
    yesterday = today - timedelta(days=1)

    if selected_cars is None:
        selected_cars = Car.query.all()

    car_count_of_day = Car.query.filter(
        Car.registration_date >= yesterday,
        Car.registration_date < today,
        Car.id.in_([car.id for car in selected_cars])  # Виправлена умова
    ).count()

    return car_count_of_day
