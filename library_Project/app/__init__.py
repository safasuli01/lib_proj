from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from app.config import config_options
from app.models import db
from flask_migrate import Migrate

def create_app(config_name='prd'):
    app = Flask(__name__)
    current_config = config_options[config_name]
    app.config.from_object(current_config)
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI

    db.init_app(app)
    migrate = Migrate(app, db)
    bootstrap = Bootstrap5(app)

    return app