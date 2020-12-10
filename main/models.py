from datetime import datetime 
from main import db
from flask_login import UserMixin 

class Base(db.Model):
    __abstract__ = True
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime,default=datetime.now, onupdate=datetime.now)
class UserBase(Base, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(20))

    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    picture = db.Column(db.String(100))
    fname = db.Column(db.String(100))
    lname = db.Column(db.String(100))
    bio = db.Column(db.Text())
    username = db.Column(db.String(10), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(20))

    # username = db.Column(db.String(10))
    role_type = db.Column(db.String(20), default="user" )
    comments = db.relationship( "Comment", backref="user", lazy=True )
    updated_at = db.Column(db.DateTime, nullable = False, default=datetime.utcnow )
    created_at = db.Column(db.DateTime, nullable = False, default=datetime.utcnow )

 
   
    def __init__(self, picture, fname, lname, bio, username, email, password):
        
        self.picture = picture
        self.fname = fname
        self.lname = lname
        self.bio = bio
        self.username = username
        self.email = email
        self.password = password
         
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.bio}')"   

company_comment = db.Table('company_comment',
       db.Column('company_id', db.Integer, db.ForeignKey('company.id'), primary_key=True),
       db.Column('comment_id', db.Integer, db.ForeignKey('comment.id'), primary_key=True )
)

class Company(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    picture = db.Column(db.String(100))
    name = db.Column(db.String(100), nullable=False, unique=True)
    bio = db.Column(db.Text())
    specialization = db.Column(db.String(100))
    username = db.Column(db.String(10), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(20))

    role_type = db.Column(db.String(20), default="company" )
    updated_at = db.Column(db.DateTime, nullable = False, default=datetime.utcnow )
    created_at = db.Column(db.DateTime, nullable = False, default=datetime.utcnow )

    #Relationship
    comments = db.relationship('Comment', secondary=company_comment, backref='company_review')

    def __init__(self, picture, name, bio, specialization, username, email, password):
        
        self.picture = picture
        self.name = name
        self.bio = bio
        self.specialization = specialization
        self.username = username
        self.email = email
        self.password = password

class Comment( db.Model ):
    id = db.Column(db.Integer, primary_key=True)
    commment_date = db.Column(db.DateTime, nullable = False, default=datetime.utcnow ) # newly added
    feedback = db.Column(db.Text())
    companyName = db.Column(db.String(100))
    rating = db.Column(db.Float)

    # relationships
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    # company = db.relationship('Company', secondary= company_comment)
    

    def __init__(self, feedback, companyName, rating, user_id):
        self.feedback = feedback
        self.companyName = companyName
        self.rating = rating
        self.user_id = user_id

    def __repr__(self):
        return f"Comment( '{self.companyName}' ,'{self.feedback}', '{self.commment_date}', '{self.rating}')"    