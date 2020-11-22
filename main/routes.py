
from flask import render_template, url_for, flash, redirect, request, session 
from flask_login import login_user, current_user, logout_user, login_required
from main import app, db, login_manager
from main.models import Company, User, Comment

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route("/home")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/profile")
def profile():
    return render_template('profile.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        user = User.query.filter_by( username = username, password = password ).first()
        if user is not None:
            login_user(user)
            return redirect("/profile")
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
    feedback = request.form.get('feedback', "")
    companyName = request.form.get('companyName', "")
    rating = request.form.get('rating', "")
   
    newComment = Comment(feedback, companyName, rating)
    db.session.add(newComment)
    db.session.commit()
    return redirect("/comments/")   

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

@app.route("/users/create", methods=["POST"])
def create_users():
    # picture = request.form.get('picture', "")
    fname = request.form.get('fname', "")
    lname = request.form.get('lname', "")
    bio = request.form.get('bio', "")
    username = request.form.get('username', "")
    email = request.form.get('email', "")
    password = request.form.get('password', "")
   
    newUser= User(fname, lname, bio, username, email, password)
    db.session.add(newUser)
    db.session.commit()
    return redirect("/users/") 

# read a single comment
@app.route("/users/<id>")
def get_user(id):
    user = User.query.get( int(id) )
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
    return redirect("/comments/")

# End of CRUD for users        


# CRUD for Company    

@app.route("/companies")
@login_required
def all_companies():
    allCompanies = Company.query.all()
    return render_template("Companies.html", companies = allCompanies)

@app.route("/comnpanies/create", methods=["POST"])
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
    return redirect("/companies/") 

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

# End of CRUD for Company        