from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to Simple Date App!'

if __name__=="__main__":
    import logging
    app.logger.setLevel(logging.DEBUG)

    app.run(host='127.0.0.1', port=5000, debug=True)

