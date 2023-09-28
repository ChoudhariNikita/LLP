from flask import Blueprint, render_template

# Create a Blueprint for this route
user_dashboard_app = Blueprint('user_dashboard', __name__)


@user_dashboard_app.route('/user')
def user_dash():
    return render_template('User/user_dash.html')
