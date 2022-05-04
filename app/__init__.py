from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

#create instances of the classes
db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)

    #step1: app is configured with SQLAlchemy settings
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    if not test_config:  
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    else:
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_TEST_DATABASE_URI'] = os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')

    #step2: db and migrate are initialized with app
    db.init_app(app)
    migrate.init_app(app, db)
    
    #import model
    from app.models.planet import Planet
    
    from .routes import planets_bp
    app.register_blueprint(planets_bp)
    
    return app
