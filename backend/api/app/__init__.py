import os
from flask import Flask
from app.config import config


def create_app():
    # check environment variables to see which config to load
    env = os.environ.get("FLASK_ENV", "dev")
    app = Flask(__name__)

    app.config.from_object(config[env])  # config dict is from api/config.py

    # Under production, this app is served under a url prefix of /api.
    # THIS MEANS ALL BLUEPRINTS WILL NEED TO BE PREFIXED WITH /api in development
    prefix = ''
    if env == 'docker':
        prefix = '/api'
        
    from app.bps.main import bp as main_bp
    app.register_blueprint(main_bp, url_prefix=prefix)
    return app
