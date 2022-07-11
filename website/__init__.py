
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

db = SQLAlchemy()
DB_NAME = "database.db"
mail = Mail()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'PADE_USA'
    app.config['SQLALCHEMY_DATABASE_URL'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    app.config['MAIL_SERVER']='smtp.mailtrap.io'
    app.config['MAIL_PORT'] = 2525
    app.config['MAIL_USERNAME'] = '97e041d5e367c7'
    app.config['MAIL_PASSWORD'] = 'cfaf5b99f8bafb'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    
    # with app.open_resource("modified_text_file.txt") as fp:  
    #  mail.attach("modified_text_file.txt", "text/txt", fp.read())  
    mail.init_app(app)
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app