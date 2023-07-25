from app import app
from flask import render_template, request, redirect

@app.route('/addplant')
def add_plant():
    return render_template("add_plant.html")

@app.route('/save-plant', methods=['POST'])
def save_plant():
    print(request.form)
    return redirect('/')
