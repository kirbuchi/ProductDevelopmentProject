# -*- coding: utf-8 -*-
from api import create_app

app, _ = create_app()

if __name__ == '__main__':
    app.run()
