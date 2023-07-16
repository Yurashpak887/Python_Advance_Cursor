from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<p> Hello s </p>'

if __name__=="__main__":
    import logging
    app.logger.setLevel(logging.DEBUG)

    app.run(host='127.0.0.1', port=5000, debug=True)

