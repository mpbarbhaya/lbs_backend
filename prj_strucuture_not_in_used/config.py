import os

class Config:
    SECRET_KEY = "flask_lbs***@123*key"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///lbs.db'
    SQLALCHEMY_TRACK_MODIFICATION = False