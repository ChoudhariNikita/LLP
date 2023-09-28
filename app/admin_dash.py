from flask import Blueprint, render_template

# Create a Blueprint for this route
admin_dashboard_app = Blueprint('admin_dashboard', __name__)


@admin_dashboard_app.route('/admin')
def admin_dashboard():
    return render_template('Admin/admin_dash.html')
