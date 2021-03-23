from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask("DatabaseApp")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite'

#ORM = Object Relational Mapper
db = SQLAlchemy(app)