from app import app
from flask import render_template, request, redirect


@app.route('/add_saloon')
def addsaloon():
    return render_template('add_saloon.html')

@app.route('/save-saloon', methods=['POST'])
def save_saloon():

    return redirect('/')