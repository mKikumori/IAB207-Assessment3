#from package import Class
from flask import Flask 
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db=SQLAlchemy()

#create a function that creates a web application
# a web server will run this web application
def create_app():
  
    app=Flask(__name__)  # this is the name of the module/package that is calling this app
    app.debug=True
    app.secret_key='somesecretgoeshere'
    #set the app configuration data 
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mydbname.sqlite'
    #initialise db with flask app
    db.init_app(app)

    Bootstrap5(app)

    #config upload folder
    UPLOAD_FOLDER = '/static/image'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    
    #initialize the login manager
    #login_manager = LoginManager()
    
    #set the name of the login function that lets user login
    # in our case it is auth.login (blueprintname.viewfunction name)
    #login_manager.login_view='auth.login'
    #login_manager.init_app(app)

    #create a user loader function takes userid and returns User
    #from .models import User  # importing here to avoid circular references
    #@login_manager.user_loader
    #def load_user(user_id):
    #    return User.query.get(int(user_id))

    #importing views module here to avoid circular references
    # a common practice.
    from . import views
    app.register_blueprint(views.mainbp)

    from . import auth
    app.register_blueprint(auth.authbp)

    from . import music_shows
    app.register_blueprint(music_shows.destbp)
    
    return app



