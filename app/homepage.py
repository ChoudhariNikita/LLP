from flask import render_template
from app import app  # Import the app object from the current package


@app.route('/')
def homepage():
    return render_template('homepage.html')
