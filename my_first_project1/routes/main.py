from app import app, db
from flask import render_template, request, redirect, session
from models.models import Car, User


@app.context_processor
def inject_user():
    user = None
    if 'user' in session:
        user = User.query.get(session['user'])
    return {'user': user}
@app.route('/')
def main():
    car = Car.query.all()
    return render_template('index.html',  cars=car)

@app.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        name = request.form.get('username')
        phone_number = request.form.get('phone_number')
        password = request.form.get('password')
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
                return redirect ('/')
        else:
            return redirect('/')

    return render_template('login.html')
