"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from ResumeBestMatch import app
from flask import request

@app.route('/')
def home():
    """Renders the home page."""
    return "Welcome"

@app.route('/search', methods=["GET"])
def search():
    """Renders the search page."""
    context= request.args.get("context")
    category= request.args.get("category")
    threshold= request.args.get("threshold")
    noOfMatches= request.args.get("noOfMatches")
    inputPath= request.args.get("inputPath")
    output_string = context +" "+category+" "+threshold+" "+noOfMatches+" "+inputPath
    return output_string

@app.route('/ping')
def ping():
    return "200"
