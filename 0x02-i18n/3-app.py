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
    """Language configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
"""Load configuration settings"""


@app.route('/')
def index_0():
    """Function that renders the index template."""
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """Get the best matching locale for the user."""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == '__main__':
    app.run(debug=True)
