from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sepkil_shox08'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cazgerhcnnyesv:a25e583b812762410876c3d918207843e2931b73fb42ff919cad55c3bd2dc8ce@ec2-44-213-228-107.compute-1.amazonaws.com:5432/dfv44jbj5g77g1'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Users, Notes
    
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))

    return app


def create_database(app):
    db.create_all(app=app)
    print('Created Database!')
