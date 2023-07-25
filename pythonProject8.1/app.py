from flask import Flask, request, jsonify
import time
app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to Simple Calculate'

@app.route('/calculate/<int:one>.<icon>.<int:two>')
def calculate(one, icon, two):
    current_time = time.time()

    if icon == "+":
        result = one + two
    elif icon == "-":
        result = one - two
    return jsonify(results=result, time=current_time)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
