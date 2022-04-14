from flask import Flask

from flask_mysqldb import MySQL

db=MySQL()

upload_folder='/home/ares/tasfia_israt_final_project/website/static/img'
def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='MIZAN'
    app.config['UPLOAD_FOLDER']=upload_folder

    app.config['MYSQL_HOST'] = '127.0.0.1'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'interior_design_and_shop'

    db.init_app(app)

    from .auth import auth
    from .interior import interior
    from .admin import admin
    from .shop import shop

    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(interior, url_prefix='/')
    app.register_blueprint(admin, url_prefix='/')
    app.register_blueprint(shop, url_prefix="/")

    return app
