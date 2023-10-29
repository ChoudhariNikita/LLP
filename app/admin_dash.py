import mysql.connector
from flask import Flask, render_template, request, flash, Blueprint, session

# Create a Blueprint for this route
admin_dashboard_app = Blueprint('admin_dashboard', __name__)

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Add your own secret key

MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'adminroot@123'
MYSQL_DB = 'fluentfusion'

mydb = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DB
)

mycursor = mydb.cursor()


@admin_dashboard_app.route('/admin')
def admin_dashboard():
    return render_template('Admin/admin_dash.html')


@admin_dashboard_app.route('/manage_users')
def manage_users():
    return render_template('Admin/manage_users.html')


@admin_dashboard_app.route('/manage_courses')
def manage_courses():
    return render_template('Admin/manage_courses.html')


@admin_dashboard_app.route('/add_course', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        teacher_id = request.form['teacher_id']
        try:
            sql = "INSERT INTO course (title, description, teacher_id) VALUES (%s, %s, %s)"
            val = (title, description, teacher_id)
            mycursor.execute(sql, val)
            mydb.commit()
            # Flash success message
            flash('Course added successfully!', 'success')
            return render_template('Admin/add_course.html')
        except mysql.connector.Error as err:
            flash(f"An error occurred: {err}", 'error')  # Flash error message
    return render_template('Admin/add_course.html')


@admin_dashboard_app.route('/view_courses')
def view_courses():
    try:
        mycursor.execute("SELECT * FROM course")
        courses = mycursor.fetchall()
        return render_template('Admin/view_courses.html', courses=courses)
    except mysql.connector.Error as err:
        flash(f"An error occurred: {err}", 'error')  # Flash error message
        return render_template('Admin/view_courses.html')


@admin_dashboard_app.route('/add_user')
def add_user():
    return render_template('Admin/add_user.html')


if __name__ == '__main__':
    app.register_blueprint(admin_dashboard_app)
    app.run(debug=True)
