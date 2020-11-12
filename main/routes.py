
from flask import render_template, url_for, flash, redirect, request, session 
from main import app, db
from main.models import Company, User, Comment

@app.route("/home")
@app.route("/")
def index():
    return render_template('index.html')


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
        return render_template("comment_comment.html", comment = comment)

# Delete
@app.route("/comments/<id>/delete", methods=["POST"])
def delete_user(id):
    user = User.query.get( int(id) )
    db.session.delete(user)
    db.session.commit()
    return redirect("/comments/")