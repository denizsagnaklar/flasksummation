from flask_sqlalchemy import SQLAlchemy
import datetime



class Calculation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_number = db.Column(db.Integer, unique=False)
    second_number = db.Column(db.Integer, unique=False)
    result = db.Column(db.Integer, unique=False)

    def __init__(self, first_number, second_number, result):
    	self.first_number = first_number
    	self.second_number = second_number
    	self.result = result

    def __repr__(self):
    	return '<Calculation %r>' % self.first_number

