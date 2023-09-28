from flask import Blueprint, render_template

# Create a Blueprint for this route
homepage_app = Blueprint('homepage', __name__)


@homepage_app.route('/')
def homepage():
    return render_template('Home/homepage.html')
