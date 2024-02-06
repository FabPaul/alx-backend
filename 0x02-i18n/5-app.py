#!/usr/bin/env python3
"""Basic flask app"""


from flask import (
    Flask,
    render_template,
    request,
    g
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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

@app.route('/')
def index_0():
    """function that returns Welcome to Holberton"""
    return render_template('5-index.html')

@babel.localeselector
def get_locale():
    """Get locale"""
    if 'locale' in request.args:
        requested_locale = request.args['locale']
        if requested_locale in app.config['LANGUAGES']:
            return requested_locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])

def get_user():
    """Get user information from the mock database"""
    user_id =  request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None

@app.before_request
def before_request():
    """find a user if any and set it as a global on flask"""
    g.user = get_user()

@app.before_request
def before_request():
    """Execute before all other functions"""
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None


if __name__=='__main__':
    app.run(debug=True)
