from app import app, db
import re
from flask import render_template, request, redirect, session
from models.models import Car, User, Modelcar, Mark
from helpers.helpers import *
from helpers.get_course import *

UPLOAD_FOLDER = './static/images'


@app.context_processor
def inject_user():
    user = None
    if 'user' in session:
        user = User.query.get(session['user'])
    return {'user': user}


@app.context_processor
def inject_currency_rates():
    dollar_rate = get_dollar_rate()
    euro_rate = get_euro_rate()
    return dict(dollar_rate=dollar_rate, euro_rate=euro_rate)

@app.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        name = request.form.get('username')
        phone_number = request.form.get('phone_number')
        password = request.form.get('password')
        countries = request.form.get('selected_country')
        print(countries)
        country = Country.query.all()
        phone_pattern = r'^0\d{9}$'
        if not re.match(phone_pattern, phone_number):
            phone_error = "Неправильний номер телефону. Вказано некоректний формат."
            return render_template('sign-up.html', phone_error=phone_error)

        user = User(name=name, phone_number=phone_number, password=password, country_id  = countries)
        db.session.add(user)
        db.session.commit()

        session['user'] = user.id
        return redirect('/')
    else:
        country = Country.query.all()

        return render_template('sign-up.html', country=country)


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
    selected_fuel = request.args.get("selected_fuel_type")
    selected_mileage_from = request.args.get("mileage_from")
    selected_mileage_to = request.args.get("mileage_to")
    selected_country = request.args.get("selected_country")

    #country = Country.query.all()
    marks = Mark.query.all()
    models_data = []

    if selected_mark:
        mark = Mark.query.filter_by(name=selected_mark).first()
        if mark:
            models_data = get_models_data(mark.id)  # Отримуємо дані моделей для вибраної марки

    cars_list = get_сars(selected_mark, selected_model_id, selected_year_from, selected_year_to, selected_mileage_from, selected_mileage_to, selected_fuel, selected_country)

    countries = Country.query.all()

    cars = get_sorted_cars(sort_by, cars_list)
    count_of_ads = count_of_all_car(cars)
    count_of_cars_day = count_of_cars_last_day(cars)

    dol_course = get_dollar_rate()
    eur_course = get_euro_rate()
    return render_template('index.html', cars=cars, count_of_ads=count_of_ads, count_of_cars_day=count_of_cars_day,
                           marks=marks, models_data=models_data, selected_mark=selected_mark,
                           selected_model_id=selected_model_id, selected_year_from=selected_year_from, countries=countries, selected_country=selected_country, dol_course=dol_course, eur_course=eur_course)

