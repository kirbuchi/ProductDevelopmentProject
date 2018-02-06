# -*- coding: utf-8 -*-

from flask import Flask


def create_app(config_name=None):
    from api.models import db

    app = Flask(__name__)

    if config_name:
        config_path = 'api.settings.{}'.format(config_name)
        app.config.from_object(config_path)

    db.app = app
    db.init_app(app)

    return app, db
