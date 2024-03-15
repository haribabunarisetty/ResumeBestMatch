"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from ResumeBestMatch import app

@app.route('/')
def home():
    """Renders the home page."""
    return "Welcome"

@app.route('/search')
def search():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/ping')
def ping():
    return "200"
