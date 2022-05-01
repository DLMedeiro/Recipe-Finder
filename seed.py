"""Seed file to make sample data for db."""

from models import User
from app import db
from flask_bcrypt import Bcrypt

# (venv) python seed.py

#Create tables
db.drop_all()
db.create_all()

#If table isn't empty, empty it
User.query.delete()

#Create User

hashed_pwd = bcrypt.generate_password_hash('TacoTaco').decode('UTF-8')

taco = User(email = 'taco@gamil.com', username = 'Taco', password = hashed_pwd)


# Add new user object to the session
db.session.add(taco)


# Commit 
db.session.commit()

