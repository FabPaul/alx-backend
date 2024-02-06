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
    return render_template('6-index.html')

@babel.localeselector
def get_locale():
    """Get locale"""
   # locale from URL params
    if 'locale' in request.args:
        locale_param = request.args.get('locale')
        if locale_param in  app.config['LANGUAGES']:
            return locale_param
        
    # Locale from user settings
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    
    # Locale from request header
    accept_languages = request.accept_languages.best_match(app.config['LANGUAGES'])
    if accept_languages:
        return accept_languages
    
    # Default locale
    default = app.config['BABEL_DEFAULT_LOCALE']
    return default


def get_user(user_id):
    """Get user information from the mock database"""
    return users.get(int(user_id))
   
@app.before_request
def before_request():
    """find a user if any and set it as a global on flask"""
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None

@app.before_request
def before_request():
    """Execute before all other functions"""
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None


if __name__=='__main__':
    app.run(debug=True)
