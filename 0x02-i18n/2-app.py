#!/usr/bin/env python3
"""Basic flask app"""


from flask import (
    Flask,
    render_template,
    request
)
from flask_babel import Babel


app = Flask(__name__)

babel = Babel(app)


class Config(object):
    """language class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULTLOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

@app.route('/')
def index_0():
    """function that returns Welcome to Holberton"""
    return render_template('2-index.html')

@request.accept_languages
def get_locale():
    """If the user is logged in, use the locale from the user settings"""
    user = getattr(request, 'user', None)
    if user is not None:
        return user.locale
    
    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__=='__main__':
    app.run(debug=True)
