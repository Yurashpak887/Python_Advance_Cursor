from app import app, db
from flask import render_template, request, redirect, session
from models.models import Car, User, Modelcar, Mark
import os

STATIC_FOLDER = '/static'

@app.route('/car/<int:car_id>', methods=['GET', 'POST'])
def car_details(car_id):
    if request.method == 'GET':
        car = Car.query.get(car_id)
        return render_template('car_details.html', car=car)
    else:
        return redirect("/")

def extract_filename_from_path(path):
    return os.path.basename(path)

# Додаємо функцію до контексту Jinja2
app.jinja_env.globals.update(extract_filename_from_path=extract_filename_from_path)