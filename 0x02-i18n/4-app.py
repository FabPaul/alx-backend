#!/usr/bin/env python3
"""Basic flask app"""


from flask import (
    Flask,
    render_template,
    request
)
from flask_babel import (
    Babel,
    _
)


app = Flask(__name__)

babel = Babel(app)


class Config(object):
    """language class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULTLOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

@app.route('/')
def index_0():
    """function that returns Welcome to Holberton"""
    return render_template('4-index.html')

@babel.localeselector
def get_locale():
    """Get locale"""
    if'locale' in request.args:
        requested_locale = request.args['locale']
        if requested_locale in app.config['LANGUAGES']:
            return requested_locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__=='__main__':
    app.run(debug=True)
