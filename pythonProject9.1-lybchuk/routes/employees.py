from app import app, db
from models.models import Employee, Plant
from flask import render_template, request, redirect
from sqlalchemy.exc import IntegrityError


@app.route('/employees')
def employees_home():
    employees = Employee.query.all()
    plant = Plant.query.all()
    return render_template("employees-list.html", employee=employees, plants=plant)


@app.route('/save-employee', methods=['POST'])
def save_employee():
    try:
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        plant_id = request.form.get('plant_id')
        employee = Employee(first_name=first_name, last_name=last_name, email=email, plant_id=plant_id)
        db.session.add(employee)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        error = "Така електронна пошта вже існує. Будь ласка, виберіть іншу електронну пошту."
        return render_template("employees-list.html", error=error)
    return redirect('/')
