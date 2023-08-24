from app import app, db
import re
from flask import render_template, request, redirect, session
from models.models import Car, User, Modelcar, Mark
from helpers.helpers import *

UPLOAD_FOLDER = './static/images'


@app.context_processor
def inject_user():
    user = None
    if 'user' in session:
        user = User.query.get(session['user'])
    return {'user': user}


@app.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        name = request.form.get('username')
        phone_number = request.form.get('phone_number')
        password = request.form.get('password')

        phone_pattern = r'^0\d{9}$'
        if not re.match(phone_pattern, phone_number):
            phone_error = "Неправильний номер телефону. Вказано некоректний формат."
            return render_template('sign-up.html', phone_error=phone_error)

        user = User(name=name, phone_number=phone_number, password=password)
        db.session.add(user)
        db.session.commit()

        session['user'] = user.id
        return redirect('/')
    else:
        return render_template('sign-up.html')


@app.route('/session-close')
def close_session():
    session.clear()
    return redirect('/')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter(User.phone_number == request.form.get('phone_number')).first()
        if user is not None:
            if user.password == request.form.get('password'):
                session['user'] = user.id
                return redirect('/')
        else:
            log_error = "Користувача не знайдено. Перевірте правильність вхідних данних"
            return render_template('login.html', log_error=log_error)

    return render_template('login.html')


@app.route('/', methods=['GET', 'POST'])
def main():
    sort_by = request.args.get('sort_by', 'price_asc')
    selected_mark = request.args.get('selected_mark')
    selected_model_id = request.args.get('selected_model')  # Отримуємо ID моделі, а не ім'я
    selected_year_from = request.args.get("year_from")
    selected_year_to = request.args.get("year_to")
    selected_mileage_from = request.args.get("mileage_from")
    selected_mileage_to = request.args.get("mileage_to")

    marks = Mark.query.all()
    models_data = []

    if selected_mark:
        mark = Mark.query.filter_by(name=selected_mark).first()
        if mark:
            models_data = get_models_data(mark.id)  # Отримуємо дані моделей для вибраної марки

    cars_list = get_сars(selected_mark, selected_model_id, selected_year_from, selected_year_to)

    cars = get_sorted_cars(sort_by, cars_list)
    count_of_ads = count_of_all_car(cars)
    count_of_cars_day = count_of_cars_last_day(cars)

    return render_template('index.html', cars=cars, count_of_ads=count_of_ads, count_of_cars_day=count_of_cars_day,
                           marks=marks, models_data=models_data, selected_mark=selected_mark,
                           selected_model_id=selected_model_id, selected_year_from=selected_year_from)

