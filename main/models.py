
from datetime import datetime # newly added
from main import db

class User( db.Model ):
    id = db.Column(db.Integer, primary_key=True)
    picture = db.Column(db.String(100))
    fname = db.Column(db.String(100))
    lname = db.Column(db.String(100))
    bio = db.Column(db.Text())
    username = db.Column(db.String(10))
    password = db.Column(db.String(20))

    # relationships
    # company = db.relationship( "Company", backref="user" )
    comments = db.relationship( "Comment", backref="user" )

    def __init__(self, fname, lname, bio, username, password):
        self.fname = fname
        self.lname = lname
        self.bio = bio
        self.username = username
        self.password = password

company_comment = db.Table('company_comment',
       db.Column('company_id', db.Integer, db.ForeignKey('company.id'), primary_key = True ),
       db.Column('comment_id', db.Integer, db.ForeignKey('comment.id'), primary_key = True )
)

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
    # fname = db.Column(db.String(100))
    # lname = db.Column(db.String(100))
    commment_date = db.Column(db.DateTime, nullable = False, default = datetime.utcnow ) # newly added
    feedback = db.Column(db.Text())
    companyName = db.Column(db.String(100))
    rating = db.Column(db.Float, primary_key=True)

    # relationships
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    # comment = db.relationship( "Comment", backref="company" )
    comments = db.relationship('Company', secondary= company_comment)

    def __init__(self, fname, lname, text, companyName):
        self.fname = fname
        self.lname = lname
        self.text = text
        self.companyName = companyName