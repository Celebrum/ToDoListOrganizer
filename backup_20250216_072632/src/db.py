
from flask_sqlalchemy import SQLAlchemy

from src.config import Config

db = SQLAlchemy()

def init_db(app):
    app.config.from_object(Config)
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
        return db