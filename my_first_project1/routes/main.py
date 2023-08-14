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


@app.route('/')
def main():
    sort_by = request.args.get('sort_by', 'price_asc')
    cars = get_sorted_cars(sort_by)
    return render_template('index.html', cars=cars)
