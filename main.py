import mysql.connector
from app.homepage import homepage_app
from app.user_dash import user_dashboard_app
from app.admin_dash import admin_dashboard_app
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

app.register_blueprint(homepage_app)
app.register_blueprint(user_dashboard_app)
app.register_blueprint(admin_dashboard_app)

# MySQL Database Configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ankushtiwari",
    database="fluentfusion"
)

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['username']
        email = request.form['email']
        password = request.form['password']

        cursor = db.cursor()
        try:
            cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                           (name, email, password))
            db.commit()
            return redirect(url_for('login'))
        except Exception as e:
            db.rollback()  # Rollback in case of an error
            return "Registration failed: " + str(e)
        finally:
            cursor.close()
    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email == "admin@fluentfusion.com" and password == "admin":
            return redirect(url_for(''))  # Redirect to the admin dashboard

        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        user = cursor.fetchone()

        if user:
            return "Login successful"
        else:
            return "Login failed"

    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
