from flask import Blueprint, render_template

# Create a Blueprint for this route
homepage_app = Blueprint('homepage', __name__)


@homepage_app.route('/')
def homepage():
    return render_template('Home/homepage.html')


@homepage_app.route('/about')
def about():
    return render_template('Home/about.html')


@homepage_app.route('/contact')
def contact():
    return render_template('Home/contact.html')


@homepage_app.route('/register')
def register():
    return render_template('home/register.html')

@homepage_app.route('/login')
def login():
    return render_template('home/login.html')

@homepage_app.route('/userdashboard')
def user():
    return render_template('user/user_dash.html')

@homepage_app.route('/admindashboard')
def admin():
    return render_template('admin/admin_dash.html')