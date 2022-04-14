from flask import Blueprint, redirect,render_template,flash,request, session
from .__init__ import db,create_app
from .settings import info
from datetime import datetime
from werkzeug.utils import secure_filename
import os


admin=Blueprint('admin', __name__)


app=create_app()

@admin.route("/admin_login", methods=["GET","POST"])
def admin_login():
    if request.method=="POST":
        email=request.form.get('email')
        password=request.form.get('password')

        if email==info['admin_email'] and password==info['admin_password']:
            session['admin']=email
            return redirect("/dashboard")
        else:
            flash("wrong email or password", category="error")
    return render_template("admin/admin_login.html")



@admin.route("/dashboard")
def dashboard():
    if 'admin' in session:
        cur=db.connection.cursor()
        cur.execute("SELECT * FROM users")
        users=cur.fetchall()
        
        return render_template("admin/index.html",users=users)

    else:
        return redirect("/admin_login")


@admin.route("/delete_user/<int:sno>")
def delete_user(sno):
    cur=db.connection.cursor()
    cur.execute("DELETE FROM users WHERE sno=%s",(sno,))
    cur.connection.commit()
    return redirect("/dashboard")



@admin.route("/product_dashboard")
def product_dashboard():
    if 'admin' in session:
        cur=db.connection.cursor()
        cur.execute("SELECT * FROM products")
        products=cur.fetchall()
        
        return render_template("admin/product_dashboard.html",products=products)

    else:
        return redirect("/admin_login")   


@admin.route("/delete_product/<int:sno>")
def delete_product(sno):
    cur=db.connection.cursor()
    cur.execute("DELETE FROM products WHERE product_id=%s",(sno,))
    cur.connection.commit()
    return redirect("/product_dashboard")


@admin.route("/add_product", methods=["GET","POST"])
def add_product():
    if 'admin' in session:
        if request.method=="POST":
            name=request.form.get('name')
            category=request.form.get('category')
            price=request.form.get('price')
            description=request.form.get('description')
            image = request.files['image_file']
            print("mizan")
            if image.filename == '':
                flash('No selected file',category='error')
                return redirect(request.url)
            else:
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(image.filename)))
                cur=db.connection.cursor()
                cur.execute("INSERT INTO products(name,image,price,description,category,date) VALUES(%s,%s,%s,%s,%s,%s)",(name,image.filename,price,description,category,datetime.now()))
                db.connection.commit()
                return redirect("/product_dashboard")
        return render_template("admin/add_product.html")

    else:
        return redirect("/admin_login")

    
    




