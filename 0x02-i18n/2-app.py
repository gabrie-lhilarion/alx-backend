#!/usr/bin/env python3
"""
A basic Flask application with Babel
for internationalization.
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """
    Configuration class for setting available
    languages and default settings.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Selects the best match for supported languages
    using request.accept_languages.

    Returns:
        str: The best match language code.
    """
    return request.accept_languages.best_match(
        app.config['LANGUAGES']
    )


@app.route('/')
def index():
    """
    Renders the index.html template which
    displays a welcome message.

    Returns:
        str: The rendered HTML content of
        the index.html template.
    """
    return render_template('index.html')


if __name__ == '__main__':
    """
    Runs the Flask application in debug mode.
    """
    app.run(debug=True)
