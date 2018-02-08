# -*- coding: utf-8 -*-
import os

from flask import Flask
from flask_cors import CORS


def create_app(config_name=None):
    from api.models import db
    from api.views import api_views

    app = Flask(__name__)
    CORS(app)

    config_name = config_name or os.environ.get('FLASK_APP_SETTINGS_NAME')

    print('Using config_name: "{}"'.format(config_name))

    if config_name:
        config_path = 'api.settings.{}'.format(config_name)
        app.config.from_object(config_path)

    db.app = app
    db.init_app(app)

    app.register_blueprint(api_views)

    return app, db


def zappa_entry(*args, **kwargs):
    app, db = create_app()
    return app(*args, **kwargs)
