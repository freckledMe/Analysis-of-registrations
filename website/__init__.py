from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sepkil_shox08'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://epajaiekwfgwnm:2e77952fc4565b6f1d7bab646ccbeffa0727c46f6c0f276e94e2e0da623b747e@ec2-35-169-11-108.compute-1.amazonaws.com:5432/dcbcocisnc82qc'
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
