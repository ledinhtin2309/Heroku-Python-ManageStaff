from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///managestaff.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    admitday = db.Column(db.String(length=12), nullable=False, unique=True)
    opinion = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.name}'


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/managestaff')
def managestaff_page():
    items = Item.query.all()
    return render_template('managestaff.html', items=items)