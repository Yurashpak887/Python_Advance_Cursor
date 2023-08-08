from app import app, db
from flask import render_template, request, redirect, session
from models.models import Plant, User

@app.route('/')
def main():
    user = None
    admin = None
    if session.get('user', False):
        user = User.query.get(session.get('user'))

    plant = Plant.query.order_by(Plant.id.desc()).all()
    return render_template('index.html', plants=plant, user=user)

@app.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        user = User(username=username, password=password, email=email)
        db.session.add(user)
        db.session.commit()

        session['user'] = user.id
        return redirect('/')
    else:
        return render_template('sign-up.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user1 = User.query.filter(User.username == request.form.get('username')).first()
        if user1 is not None:
            if user1.password == request.form.get('password'):
                session['user'] = user1.id
                return redirect('/')  # Редірект на головну сторінку після успішної авторизації
        else:
            return redirect('/')  # Редірект назад на сторінку входу у випадку невірних даних

    return render_template('login.html')

@app.route('/session-close')
def session_close():
    session.clear()
    return redirect('/')
