from flask import Flask

app = Flask(__name__)

@app.route('/')
def basic():
    return '<p> Hello basic route</p>'

@app.route('/firstname/')
@app.route('/firstname/<name>')
def firstname(name='Nonetype'):
    return f'Hello {name}'

if __name__=="__main__":
    import logging
    app.logger.setLevel(logging.DEBUG)

    app.run(host='127.0.0.1', port=5000, debug=True)

