from flask import Blueprint,render_template
from .__init__ import db


shop=Blueprint('shop', __name__)

@shop.route('/shop')
def interior_shop():
    cur=db.connection.cursor()
    cur.execute("SELECT * FROM products")
    products=cur.fetchall()
    return render_template('shop/shop.html',products=products)


@shop.route('/detail/<int:id>')
def detail(id):
    cur=db.connection.cursor()
    cur.execute("SELECT * FROM products WHERE product_id=%s",(id,))
    single_product=cur.fetchone()
    return render_template("shop/detail.html", single_product=single_product)


@shop.route('/checkout')
def checkout():
    return render_template("shop/checkout.html")



@shop.route('/cart')
def cart():
    return render_template("shop/cart.html")

