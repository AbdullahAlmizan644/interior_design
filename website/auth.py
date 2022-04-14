from flask import Blueprint, redirect, render_template,request,flash,session
from .__init__ import db
from .settings import info
from datetime import datetime

auth=Blueprint('auth', __name__)

@auth.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")

        cur=db.connection.cursor()
        cur.execute("SELECT * FROM  users where username=%s and password=%s",(username,password,))
        user=cur.fetchone()

        if user:
            session['user']=username
            flash("successfully login!", category="success")
            return redirect("/profile")

        else:
            flash("wrong email or password", category="error")

    return render_template("auth/login.html")


@auth.route("/user_logout")
def user_logout():
    if 'user' in session:
        session.pop('user',None)
        return redirect("/")
    else:
        return redirect("/login")

@auth.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method=="POST":
        username=request.form.get('name')
        email=request.form.get('email')
        password1=request.form.get('password1')
        password2=request.form.get('password2')

        cur=db.connection.cursor()
        cur.execute("SELECT * FROM  users where email=%s",(email,))
        user_email=cur.fetchone()



        if user_email:
            flash("email already exists!", category="error")

        elif len(username)<5:
            flash("username must be larger than 5 character", category="error")

        elif len(email)<5:
            flash("email must be larger than 5 character", category="error")

        elif len(password1)<8:
            flash("password must be larger than 8 character", category="error")

        elif password1!=password2:
            flash("password doesn't match", category="error")

        else:
            flash("Account Created Successfully!", category="success")

            cur=db.connection.cursor()
            cur.execute("INSERT INTO users(username,email,password,date) VALUES (%s,%s,%s,%s)",(username,email,password1,datetime.now()))
            db.connection.commit()
            cur.close()



            return redirect("/login")


    return render_template("auth/signup.html")


@auth.route("/profile")
def profile():
    if 'user' in session:
        cur=db.connection.cursor()
        cur.execute("SELECT * FROM  users where username=%s",(session["user"],))
        user=cur.fetchone()
        print(user)
        return render_template("auth/profile.html",user=user)
    else:
        return redirect("/login")



@auth.route("/profile_edit")
def profile_edit():
    return render_template("auth/profile_edit.html")