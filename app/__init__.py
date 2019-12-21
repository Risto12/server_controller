from flask import Flask
from config import Config
from flask_migrate import Migrate
from .models import db, login
import os


migrate = Migrate()


def app_factory(config=Config):

	app = Flask(__name__)
	app.config.from_object(config)

	db.init_app(app)
	migrate.init_app(app, db)

	login.init_app(app)
	login.login_view = 'main.login'

	from .main import main_bp
	app.register_blueprint(main_bp)
	
	return app	


