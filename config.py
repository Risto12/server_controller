import os
import conf_env

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = conf_env.SECRET_KEY
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or conf_env.SQLALCHEMY_DATABASE_URI
	SQLALCHEMY_TRACK_MODIFICATIONS = False	
