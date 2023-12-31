from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import render_template

app = Flask(__name__)
app.config.from_object("config.Config")
app.secret_key = "blablabla"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

with app.app_context():
    from routes.main import *
    from routes.plants import *
    from routes.salons import *
    from routes.employees import *

# Реєстрація моделей
from models.models import Plant, Employee, User


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
