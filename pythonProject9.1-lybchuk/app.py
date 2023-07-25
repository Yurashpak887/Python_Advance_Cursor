from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@database/flask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

with app.app_context():
    from routes.main import *
    from models import models


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
