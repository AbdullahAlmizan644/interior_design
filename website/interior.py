from flask import Blueprint,render_template
from .__init__ import db

interior=Blueprint('interior', __name__)

@interior.route("/")
def index():
    return render_template("interior/index.html")



@interior.route("/team")
def team():
    return render_template("interior/team.html")


@interior.route("/pricing")
def pricing():
    return render_template("interior/pricing.html")



@interior.route("/about")
def about():
    return render_template("interior/about.html")

@interior.route("/faq")
def faq():
    return render_template("interior/faq.html")


@interior.route("/projects")
def projects():
    return render_template("interior/projects.html")


@interior.route("/news")
def news():
    return render_template("interior/news.html")



@interior.route("/service")
def service():
    return render_template("interior/service.html")

    

@interior.route("/contact")
def contact():
    return render_template("interior/contact.html")