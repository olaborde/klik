from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class User( db.Model ):
    id = db.Column(db.Integer, primary_key=True)
    picture = db.Column(db.String(100))
    fname = db.Column(db.String(100))
    lname = db.Column(db.String(100))
    bio = db.Column(db.Text())
    username = db.Column(db.String(10))
    password = db.Column(db.String(20))

    # relationships
    company = db.relationship( "Company", backref="user" )
    comment = db.relationship( "Comment", backref="user" )

    def __init__(self, fname, lname, bio, username, password):
        self.fname = fname
        self.lname = lname
        self.bio = bio
        self.username = username
        self.password = password


class Company( db.Model ):
    id = db.Column(db.Integer, primary_key=True)
    picture = db.Column(db.String(100))
    name = db.Column(db.String(100))
    bio = db.Column(db.Text())
    specialization = db.Column(db.String(100))
    username = db.Column(db.String(10))
    password = db.Column(db.String(20))

    # relationships
    comment = db.relationship( "Comment", backref="company" )
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, picture, name, bio, specialization, username, password):
        self.picture = picture
        self.name = name
        self.bio = bio
        self.specialization = specialization
        self.username = username
        self.password = password



class Comment( db.Model ):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(100))
    lname = db.Column(db.String(100))
    text = db.Column(db.Text())
    companyName = db.Column(db.String(100))
    rating = db.Column(db.Float, primary_key=True)

    # relationships
    comment = db.relationship( "Comment", backref="company" )
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, fname, lname, text, companyName):
        self.fname = fname
        self.lname = lname
        self.text = text
        self.companyName = companyName


@app.route("/")
def home():
    return render_template("index.html")

