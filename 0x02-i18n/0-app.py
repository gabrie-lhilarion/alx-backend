#!/usr/bin/env python3
"""
A basic Flask application with a single route and an index.html template.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    Renders the index.html template which displays a welcome message.

    Returns:
        str: The rendered HTML content of the index.html template.
    """
    return render_template('0-index.html')
