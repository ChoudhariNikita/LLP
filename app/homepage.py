import mysql.connector
from flask import Flask, Blueprint, request, render_template, redirect, url_for
from flask import flash
import re

# Create a Blueprint for this route
homepage_app = Blueprint('homepage', __name__)

MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'adminroot@123'
MYSQL_DB = 'fluentfusion'


@homepage_app.route('/')
def homepage():
    return render_template('Home/homepage.html')


@homepage_app.route('/about')
def about():
    return render_template('Home/about.html')


@homepage_app.route('/contact')
def contact():
    return render_template('Home/contact.html')


@homepage_app.route('/register_page', methods=['GET', 'POST'])
def register_page():
    return render_template('Home/register.html')


@homepage_app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('Home/login.html')


@homepage_app.route('/userdashboard')
def user():
    return render_template('User/user.html')


@homepage_app.route('/admindashboard')
def admin():
    flash('Welcome Admin!')
    return render_template('Admin/admin.html')


# @homepage_app.app_errorhandler(404)
# def page_not_found(error):
#     return render_template('page_not_found.html'), 404


app = Flask(__name__)

# Establish connection
mydb = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DB
)

# Create cursor
mycursor = mydb.cursor()

# Function to add user details to the database


def add_user(name, email, password, country):
    # Simple password security check
    if len(password) < 8:
        return "Password should be at least 8 characters long."

    mycursor.execute("SELECT * FROM User WHERE email = %s", (email,))
    existing_user = mycursor.fetchone()
    if existing_user:
        flash("Account already exists. Please try logging in.")
        return render_template('Home/login.html')
    elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        flash('Invalid email address !')
    elif not re.match(r'[A-Za-z0-9]+', password):
        flash('Password must contain characters and numbers!')
    elif not name or not password or not email:
        flash('Please fill out the form !')

    sql = "INSERT INTO User (name, email, password, country) VALUES (%s, %s, %s, %s)"
    val = (name, email, password, country)
    mycursor.execute(sql, val)
    mydb.commit()

# Registration route


@homepage_app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        country = request.form['country']

        try:
            print(f"Received data: {name}, {email}, {password}, {country}")
            add_user(name, email, password, country)
            flash('You have successfully registered!')
            return render_template('Home/login.html')
        except Exception as e:
            print(f"Registration failed: {e}")
            flash(f"Registration failed: {e}")

    return render_template('Home/register.html')

# Login route


@homepage_app.route('/login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email == "admin@fluentfusion.com" and password == "fluentadmin@123":
            # Redirect to the admin dashboard
            return render_template('Admin/admin.html')

        mycursor = mydb.cursor()
        mycursor.execute(
            "SELECT * FROM User WHERE email = %s AND password = %s", (email, password))
        user = mycursor.fetchone()

        if user:
            return redirect(url_for('user'))
        else:
            flash("Login failed: User not found.")
            return render_template('Home/login.html')

    return render_template('Admin/admin.html')


if __name__ == '__main__':
    app.run(debug=True)
