from app import app, db
from flask import render_template, request, redirect, session, url_for, flash
from models.models import Car, User, Mark, Modelcar
from helpers.helpers import *


@app.route('/user-dashboard', methods=['GET', 'POST'])
def get_info():
    if 'user' in session:
        user = User.query.get(session['user'])
        sorted_cars = request.args.get('sort_by', default=None)
        cars = Car.query.filter_by(
            user_id=user.id).all()  # Отримати всі автомобілі, які належать авторизованому корвачеві
        cars = get_sorted_cars(sorted_cars,cars)
        return render_template('user-dashboard.html', user=user, cars=cars, get_sorted_cars=get_sorted_cars)
    return redirect('/login')  # Якщо користувач не авторизований, перенаправити його на сторінку входу


@app.route('/delete-car/<int:car_id>', methods=['GET', 'POST'])
def delete_car(car_id):
    car = Car.query.get(car_id)
    if car.user_id == session['user']:
        db.session.delete(car)
        db.session.commit()
    return redirect(url_for('get_info'))





