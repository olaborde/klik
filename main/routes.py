
from flask import render_template, url_for, flash, redirect, request, session 
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from main import app, db, login_manager
from main.models import Company, User, Comment
from sqlalchemy import create_engine


engine = create_engine('sqlite:///database.db', connect_args={'check_same_thread': False})
conn = engine.raw_connection()
# cursor = conn.cursor()

# @login_manager.user_loader
# def load_user(user_id, session):
#   if session['role_type'] == 'Company':
#       return Company.query.get(int(user_id))
#   elif session['role_type'] == 'User':
#       return User.query.get(int(user_id))
#   else:
#       return None

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
# @login_manager.user_loader
# def load_user(user_id,role_type):
#     if role_type == 'company':
#         return Company.query.get(user_id)
#     return User.query.get(user_id)    


@app.route("/home")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route("/profile")
@login_required
def profile():
    return render_template('profile.html', user = current_user)



# @app.route("/signup")
# def signup():
#     return render_template('signup.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        user = User.query.filter_by( username = username, password = password ).first()
        if user:
            login_user(user)
            return redirect("/profile")
        else:
            return redirect("/login")    
    else:
        return render_template('login.html')

@app.route("/company_login", methods=['GET', 'POST'])
def company_login():
    if request.method == "POST":
        print("--------------Post method----------------------")
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        print("-------------Username --> "+username+"-----------Password-->"+password+"-----------------")
        company = Company.query.filter_by( username = username, password = password ).first()
        
        if company:
            print("--------------Company is not empty----------------------")
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
    user = User.query.get( int(id) )
    db.session.delete(user)
    db.session.commit()
    return redirect("/comments/")
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
def get_user(id):
    user = User.query.get( id )
    #TODO: Create view for comment
    return render_template("comment.html", user = user)     

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
@app.route("/companies/<id>/edit", methods=["GET", "POST"])
def edit_comnpany(id):
    company = Company.query.get( int(id) )
    if request == "Post":
        picture = request.form.get('picture', "")
        name = request.form.get('name', "")
        bio = request.form.get('bio', "")
        specialization = request.form.get('specialization', "")
        username = request.form.get('username', "")
        email = request.form.get('email', "")
        password = request.form.get('password', "")
        
        db.session.commit()
        return render_template("company.html", company = company)
    else:
        return render_template("edit_company.html", company = company)

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