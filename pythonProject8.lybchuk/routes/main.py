from app import app
from flask import render_template
@app.route("/")
def hello():
    return "Ok"

@app.route('/hello/<name>')
def hellouser(name):
    return render_template('index.html', name=name)
