import mysql.connector
from flask import Flask,Blueprint, request, render_template
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB

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
    sql = "INSERT INTO User (name, email, password, country) VALUES (%s, %s, %s, %s)"
    val = (name, email, password, country)
    mycursor.execute(sql, val)
    mydb.commit()

# Route to handle the registration form submission


@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        # Hash this before storing in the database
        password = request.form.get('password')
        country = request.form.get('country')

        add_user(name, email, password, country)
        print("User details added to the database.")
        return "User successfully registered."


if __name__ == '__main__':
    app.run(debug=True)
