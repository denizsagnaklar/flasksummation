from flask import Flask, request, render_template, redirect, url_for
from flask_wtf import FlaskForm 
from wtforms import FloatField
from wtforms.validators import *
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

POSTGRES = {
    'db': 'sum_db',
    'host': 'localhost',
    'port': '5432',
}

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'dsfdsajdfsafodskmvok'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(host)s:%(port)s/%(db)s' % POSTGRES

db = SQLAlchemy(app)

class Calc(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_number = db.Column(db.Integer, unique=False)
    second_number = db.Column(db.Integer, unique=False)
    result = db.Column(db.Integer, unique=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, first_number, second_number, result):
        self.first_number = first_number
        self.second_number = second_number
        self.result = result



@app.route('/')
def index():
    return render_template('index.jinja2')

@app.route('/summation', methods=['GET', 'POST'])
def summation():
    db.create_all()
    class DivideForm(FlaskForm):
        first = FloatField("First Number: ", validators=[NumberRange(min=None, message="Input must be a number."), InputRequired(message="Input is required.")])
        second = FloatField("Second Number: ", validators=[NumberRange(min=None, message="Input must be a number."), InputRequired(message="Input is required.")])

    form = DivideForm()
    result = None
    calculation = None

    if form.validate_on_submit():
        result = form.first.data + form.second.data

    calculation = Calc(form.first.data, form.second.data, result)
    db.session.add(calculation)
    db.session.commit()
    return render_template('summation.jinja2', result=result, form=form)

@app.route('/history', methods=['GET', 'POST'])
def history():
    myCalcs = Calc.query.all()
    return render_template('history.jinja2', myCalcs=myCalcs)

if __name__ == '__main__':
    app.debug = True
    app.run()

db.drop_all()
















