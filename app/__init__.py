from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlalchemy

#create instances of the classes
db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)

    #step1: app is configured with SQLAlchemy settings
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development'

    #step2: db and migrate are initialized with app
    db.init_app(app)
    migrate.init_app(app, db)
    
    #import model
    from app.models.planet import Planet
    
    
    from .routes import planets_bp
    app.register_blueprint(planets_bp)
    
    return app
