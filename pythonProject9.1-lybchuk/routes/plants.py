from app import app, db
from flask import render_template, request, redirect
from models.models import Plant, Employee

@app.route('/add_plant')
def add_plant():
    employees = Employee.query.all()
    return render_template("add_plant.html", employee=employees)

@app.route('/save-plant', methods=['POST'])
def save_plant():
    name = request.form.get('name')
    location = request.form.get('location')
    plant = Plant(title=name, location=location)
    db.session.add(plant)
    db.session.commit()
    print(request.form)
    return redirect('/')

@app.route('/delete-plant/<int:id>')
def delete_plant(id):
    plant = Plant.query.get(id)
    db.session.delete(plant)
    db.session.commit()
    return redirect('/')

@app.route('/edit-plant/<int:id>')
def edit_plant(id):
    plant = Plant.query.get(id)
    return render_template('add_plant.html', plant=plant)

@app.route('/update-plant/<int:id>', methods=['POST'])
def update_plant(id):
    plant = Plant.query.get(id)
    plant.title = request.form.get('name')
    plant.location = request.form.get('location')
    db.session.add(plant)
    db.session.commit()
    return redirect('/')

