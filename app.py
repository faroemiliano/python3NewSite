from flask import Flask, request, render_template, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from db import db

app = Flask(__name__)
#mi coneccion con PSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:password@localhost:5433/sitioweb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
app.secret_key = "mysecretkey"

from modules.home import controller
from modules.login import controller
from modules.products import controller

if __name__ == "__main__":
    app.run(port=3000, debug=True) 

    