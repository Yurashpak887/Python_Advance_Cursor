from app import app, db
from flask import render_template, request, redirect, session
from models.models import Car, User


@app.route('/user-dashboard', methods=['GET', 'POST'])
def get_info():
    if 'user' in session:
        user = User.query.get(session['user'])
    return render_template('user-dashboard.html', user=user)