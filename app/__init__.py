from app import homepage, user_dash, admin_dash
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure your MySQL or MongoDB database here
# For MySQL example:
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/dbname'
db = SQLAlchemy(app)
