from app import app, db
from flask import render_template, request, redirect, session
from models.models import Car

from werkzeug.utils import secure_filename
import os

# ...

UPLOAD_FOLDER = './static/images'


@app.route('/add_car', methods=['GET', 'POST'])
def add_car():
    if request.method == 'POST':
        # Отримання даних з форми
        name = request.form.get('name')
        model = request.form.get('model')
        price = request.form.get('price')
        description = request.form.get('description')
        year = request.form.get('year')
        mileage = request.form.get('mileage')
        engine = request.form.get('engine')

        # Збереження зображення
        image = request.files['image']
        if image:
            filename = secure_filename(image.filename)
            image_path = os.path.join(UPLOAD_FOLDER, filename)
            image.save(image_path)



        author_id = None
        if 'user' in session:
            author_id = session['user']

        # Збереження даних в БД
        new_car = Car(name=name, model=model, price=price, description=description,
                      year=year, mileage=mileage, engine=engine, image_url=image_path, user_id = author_id)
        db.session.add(new_car)
        db.session.commit()

        return redirect('/')

    return render_template('add_car.html')
