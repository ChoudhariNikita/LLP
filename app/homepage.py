import mysql.connector
from flask import Flask, Blueprint, request, render_template
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB
import hashlib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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
    hashed_password = hashlib.sha256(
        password.encode()).hexdigest()  # Hash the password
    sql = "INSERT INTO User (name, email, password, country) VALUES (%s, %s, %s, %s)"
    val = (name, email, hashed_password, country)
    mycursor.execute(sql, val)
    mydb.commit()

# Route to handle the registration form submission


def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirmPassword')
        country = request.form.get('country')

        # Simple form validation example
        if not all([name, email, password, confirm_password, country]):
            return "Please fill in all the fields."

        if password != confirm_password:
            return "Passwords do not match."

        # Add more complex validation as per your requirements

        # Add the user if validation passes
        add_user(name, email, password, country)
        send_email(email)
        print("User details added to the database.")
        return "User successfully registered."


def send_email(user_email):
    sender_email = "your_email@gmail.com"  # Your email
    receiver_email = user_email
    password = "your_password"  # Your email account password

    message = MIMEMultipart("alternative")
    message["Subject"] = "Registration Successful"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    Thank you for registering."""

    html = """\
    <html>
      <body>
        <p>Hi,<br>
           Thank you for registering.
        </p>
      </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


if __name__ == '__main__':
    app.run(debug=True)
