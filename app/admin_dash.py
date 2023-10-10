from flask import Blueprint, render_template

# Create a Blueprint for this route
admin_dashboard_app = Blueprint('admin_dashboard', __name__)


@admin_dashboard_app.route('/admin')
def admin_dashboard():
    return render_template('Admin/admin_dash.html')

@admin_dashboard_app.route('/manage_users')
def manage_users():
    return render_template('Admin/manage_users.html')

@admin_dashboard_app.route('/manage_courses')
def manage_courses():
    return render_template('Admin/manage_courses.html')

@admin_dashboard_app.route('/add_user')
def add_user():
    return render_template('Admin/add_user.html')

@admin_dashboard_app.route('/add_course')
def add_course():
    return render_template('Admin/add_course.html')
