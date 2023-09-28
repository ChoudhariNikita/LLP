from flask import render_template
from app import app


@app.route('/admin')
def admin_dashboard():
    return render_template('Admin/admin_dash.html')
