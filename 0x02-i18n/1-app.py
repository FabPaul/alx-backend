#!/usr/bin/env python3
"""Basic flask app"""


from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)

babel = Babel(app)


class Config(object):
    """language class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULTLOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
"""load config settings"""


@app.route('/')
def index_0():
    """function that returns Welcome to Holberton"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
