import mysql.connector
from flask import Flask, Blueprint, request, render_template, redirect, url_for

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


@homepage_app.route('/register')
def register_page():
    return render_template('home/register.html')


@homepage_app.route('/login')
def login():
    return render_template('home/login.html')


@homepage_app.route('/userdashboard')
def user():
    return render_template('user/user.html')


@homepage_app.route('/admindashboard')
def admin():
    return render_template('admin/admin.html')


app = Flask(__name__)
app.register_blueprint(homepage_app)

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
    if len(password) < 6:
        return "Password should be at least 6 characters long."

    sql = "INSERT INTO User (name, email, password, country) VALUES (%s, %s, %s, %s)"
    val = (name, email, password, country)
    mycursor.execute(sql, val)
    mydb.commit()

# Registration route
# Registration route


@app.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        try:
            # Replace "Country" with the actual country
            add_user(name, email, password, "Country")
            return redirect(url_for('login'))
        except Exception as e:
            return "Registration failed: " + str(e)

    return render_template('register.html')

# Login route


@app.route('/login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email == "admin@fluentfusion.com" and password == "fluentadmin@123":
            # Redirect to the admin dashboard
            return redirect(url_for('admin'))

        cursor = mydb.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        user = cursor.fetchone()

        if user:
            return "Login successful"
        else:
            return "Login failed"

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
