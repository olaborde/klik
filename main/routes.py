
from flask import render_template, url_for, flash, redirect, request, session
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from main import app, db, login_manager
from main.models import User, Company, Comment
from sqlalchemy import create_engine
import flask_excel as excel


excel.init_excel(app) # required since version 0.0.7
engine = create_engine('sqlite:///database.db', connect_args={'check_same_thread': False})
conn = engine.raw_connection()
# cursor = conn.cursor()

@login_manager.user_loader
def load_user(user_id):
    login_type = session.get('login_type')
   
    if login_type == 'user':
        return User.query.get(user_id)
    elif login_type == 'company':
        return Company.query.get(user_id)
    else:
        return User.query.get(user_id)   


@app.route("/home")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/dashboard",  methods=['GET', 'POST'])
@login_required
def dashboard():
    company_review = Comment.query.filter((Comment.companyName==current_user.name)).all()
    return render_template('dashboard.html', company_review=company_review)

    print('%%%%%%%%%%%%%%%%%%', company_review)
    ratings = []
    average_rating = None
    for comments in company_review:
        ratings.append(comments.rating)
        average_rating = sum(ratings) / len(ratings)
    return render_template('dashboard.html', company_review=company_review, average= average_rating)


@app.route("/profile")
@login_required
def profile():
    user_review = Comment.query.filter((Comment.user_id==current_user.id)).all()
    return render_template('profile.html', user_review=user_review)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        user = User.query.filter_by( username = username, password = password ).first()
        if user:
            session['login_type'] = 'user'
            login_user(user)
            return redirect("/profile")
        else:
            return redirect("/login")    
    else:
        return render_template('login.html')

@app.route("/company_login", methods=['GET', 'POST'])
def company_login():
    if request.method == "POST":
        
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        company = Company.query.filter_by( username = username, password = password ).first()
        
        if company:
            session['login_type'] = 'company'
            login_user(company)
            return redirect("/dashboard")
        else:
            return redirect("/login")    
    else:
        return render_template('login.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")

# CRUD for comments 
@app.route("/comments")
def all_comments():
    all_comments = Comment.query.all()
    return render_template('comments.html', comments=all_comments)

@app.route("/comments/create", methods=["POST"])
def create_comments():
    companyName = request.form.get('companyName', "")
    user_id = request.form.get('user_id', "")
    feedback = request.form.get('feedback', "")
    companyName = request.form.get('companyName', "")
    rating = request.form.get('rating', "")
    newComment = Comment(feedback, companyName, rating, user_id)
    db.session.add(newComment)
    db.session.commit()
    return redirect("/")

#Update Comment
@app.route("/comments/update",  methods=["POST"])    
def update_comments():
    comments = request.form.get("user_id")
    updated_companyName = request.form.get('companyName')
    updated_feedback = request.form.get('feedback')
    updated_rating = request.form.get('rating')

    comment = Comment.query.filter_by(id=comments).first() 
    comment.feedback = updated_feedback
    comment.rating = updated_rating
    comment.companyName = updated_companyName
    db.session.commit()
    return redirect('/profile')

# read a single comment
@app.route("/comments/<id>")
def get_comment(id):
    comment = Comment.query.get( int(id) )
    #TODO: Create view for comment
    return render_template("comment.html", comment = comment)     

#Update 
@app.route("/comments/<id>/edit", methods=["GET", "POST"])
def edit_comment(id):
    comment = Comment.query.get( int(id) )
    if request == "Post":
        comment.feedback = request.form.get('feedback', "")
        comment.companyName = request.form.get('companyName', "")
        comment.rating = request.form.get('rating', "")
        
        db.session.commit()
        return render_template("comment.html", comment = comment)
    else:
        return render_template("edit_comment.html", comment = comment)

# Delete
@app.route("/comments/<id>/delete", methods=["POST"])
def delete_comment(id):
    comment = Comment.query.get( int(id) )
    db.session.delete(comment)
    db.session.commit()
    return redirect("/profile")
# End of CRUD comment

# CRUD for users    

@app.route("/users")
@login_required
def all_users():
    allUsers = User.query.all()
    return render_template("users.html", users = allUsers)

@app.route('/signup_user', methods=['GET', 'POST'])
def signup_user():
    if request.method == "POST":
        # return redirect(url_for('index'))
        picture = request.form.get('picture', "")
        fname = request.form.get('fname', "")
        lname = request.form.get('lname', "")
        bio = request.form.get('bio', "")
        username = request.form.get('username', "")
        email = request.form.get('email', "")
        password = request.form.get('password', "")
   
        newUser= User(picture, fname, lname, bio, username, email, password)
        db.session.add(newUser)
        db.session.commit()
        # session['role_type'] == 'user'
        return redirect("/login") 
    else:
        return render_template('signup.html') 

#Update User
@app.route("/users/update",  methods=["POST"])    
def update_user():
    user_id = request.form.get("user_id")   
    updated_picture = request.form.get('picture')
    updated_fname = request.form.get('fname')
    updated_lname = request.form.get('lname')
    updated_bio = request.form.get('bio')
    updated_username = request.form.get('username')
    updated_email = request.form.get('email')
    updated_password = request.form.get('password') 

    user = User.query.filter_by(id=user_id).first()  
    user.picture = updated_picture
    user.fname = updated_fname
    user.lname = updated_lname
    user.bio = updated_bio
    user.username = updated_username
    user.email = updated_email
    user.password = updated_password
    db.session.commit()
    return redirect('/profile')


# read a single comment
@app.route("/users/<id>")
def singleUser(id):
    user = User.query.get( id )
    #TODO: Create view for comment
    return render_template("singleUser.html", user = user)     

#Update user
@app.route("/users/<id>/edit", methods=["GET", "POST"])
def edit_user(id):
    user = User.query.get( int(id) )
    if request == "Post":
        # picture = request.form.get('picture', "")
        fname = request.form.get('fname', "")
        lname = request.form.get('lname', "")
        bio = request.form.get('bio', "")
        username = request.form.get('username', "")
        email = request.form.get('email', "")
        password = request.form.get('password', "")
        
        db.session.commit()
        return render_template("user.html", user = user)
    else:
        return render_template("edit_user.html", user = user)

# Delete user
@app.route("/users/<id>/delete", methods=["POST"])
def delete_user(id):
    user = User.query.get( int(id) )
    db.session.delete(user)
    db.session.commit()
    return redirect("/login")

# End of CRUD for users        


# CRUD for Company    

@app.route("/companies")
@login_required
def all_companies():
    allCompanies = Company.query.all()
    return render_template("Companies.html", companies = allCompanies)

@app.route("/companies/create", methods=["POST"])
def create_company():
    picture = request.form.get('picture', "")
    name = request.form.get('name', "")
    bio = request.form.get('bio', "")
    specialization = request.form.get('specialization', "")
    username = request.form.get('username', "")
    email = request.form.get('email', "")
    password = request.form.get('password', "")
   
    # company = Company("dummy pic", "Evil Corp", "zap", "take yo money", "Ecorp", "ecorp@gmail.com", "mazzaradi")
    newCompany= Company(picture, name, bio, specialization, username, email, password)
    db.session.add(newCompany)
    db.session.commit()
    return redirect("/login") 

# read a single comment
@app.route("/companies/<id>")
def get_company(id):
    company = Company.query.get( int(id) )
    #TODO: Create view
    return render_template("comment.html", company = company)     

#Update company
@app.route("/companies/update", methods=["POST"])
def edit_comnpany():
    company_id = request.form.get("company_id")
    company = Company.query.filter_by( id=company_id).first()
    
    company.picture = request.form.get('picture', "")
    company.name = request.form.get('name', "")
    company.bio = request.form.get('bio', "")
    company.specialization = request.form.get('specialization', "")
    company.username = request.form.get('username', "")
    company.email = request.form.get('email', "")
    companypassword = request.form.get('password', "")
        
    db.session.commit()
    return redirect("/dashboard")


# Delete company
@app.route("/companies/<id>/delete", methods=["POST"])
def delete_company(id):
    company = Company.query.get( int(id) )
    db.session.delete(company)
    db.session.commit()
    return redirect("/companies/")


# Recently search bar route, by Jose
@app.route("/search", methods=['GET', 'POST'])
@app.route('/companies/search', methods=['GET', 'POST'])
def search():
    companyName = request.args.get('companyName',"")
    if companyName != "":
        query_stmt = "SELECT * FROM company WHERE name LIKE '%{}%';".format(companyName.replace('"', '""'))
        cursor = conn.cursor()
        cursor.execute(query_stmt)
        conn.commit()
        data = cursor.fetchall()
        # All in the search box will return all the tuples
        if len(data) == 0 and companyName == 'all': 
            cursor.execute("SELECT * from company")
            conn.commit()
            data = cursor.fetchall()
        return render_template('search.html', data=data, user = current_user)
    return render_template('search.html')
# end point for inserting data dynamicaly in the database

# Export review to excel
@app.route("/export", methods=['GET'])
def doexport():
    column_names = ['feedback', 'rating', 'user_id', 'commment_date']
    company_review = Comment.query.filter((Comment.companyName==current_user.name)).all()
 
    return excel.make_response_from_query_sets(company_review, column_names, "xls")