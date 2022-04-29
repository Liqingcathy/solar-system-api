from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlalchemy

#gives access to db operations and updating db
db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)

    #step1: DB config and connect to db
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development'

    #step2: connect db and migrate with flask app
    db.init_app(app)
    migrate.init_app(app, db)
    
    from app.models.planet import Planet
    #import model
    
    
    from .routes import planets_bp
    app.register_blueprint(planets_bp)
    
    return app
