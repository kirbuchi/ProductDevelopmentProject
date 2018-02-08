# -*- coding: utf-8 -*-

from api import create_app

if __name__ == '__main__':
    _, db = create_app()
    db.drop_all()
    db.create_all()
