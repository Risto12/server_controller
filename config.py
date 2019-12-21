import os
import env

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = env.SECRET_KEY
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or env.SQLALCHEMY_DATABASE_URI
	SQLALCHEMY_TRACK_MODIFICATIONS = False	
