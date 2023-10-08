from flask import Blueprint, render_template

# Create a Blueprint for this route
user_dashboard_app = Blueprint('user_dashboard', __name__)


@user_dashboard_app.route('/user')
def user_dash():
    return render_template('User/user_dash.html')

@user_dashboard_app.route('/courses')
def courses():
    return render_template('user/courses.html')

@user_dashboard_app.route('/reg_courses')
def reg_courses():
    return render_template('user/reg_courses.html')

@user_dashboard_app.route('/profile')
def profile():
    return render_template('user/profile.html')