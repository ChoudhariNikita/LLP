from flask import render_template
from app import app


@app.route('/user')
def user_dash():
    return render_template('User/user_dash.html')
