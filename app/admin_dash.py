from flask import redirect, url_for
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


@admin_dashboard_app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    if request.method == 'POST':
        current_password = request.form['current_password']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        # Add validation for the new password
        if new_password != confirm_password:
            flash('New password and confirm password do not match!', 'error')
        elif len(new_password) < 8:
            flash('Password should be at least 8 characters long.', 'error')
        else:
            try:
                # Assuming you have stored the user ID in the session
                user_id = session['id']
                print(user_id)
                mycursor.execute(
                    "SELECT password FROM user WHERE id = %s", (user_id,))
                row = mycursor.fetchone()
                if row and row[0] == current_password:
                    sql = "UPDATE user SET password = %s WHERE id = %s"
                    mycursor.execute(sql, (new_password, user_id))
                    mydb.commit()
                    flash('Password changed successfully!', 'success')
                else:
                    flash('Incorrect current password. Please try again.', 'error')
            except mysql.connector.Error as err:
                flash(f"An error occurred: {err}", 'error')
    return render_template('Admin/change_password.html')


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
        print(courses)
        return render_template('Admin/view_courses.html', courses=courses)
    except mysql.connector.Error as err:
        flash(f"An error occurred: {err}", 'error')  # Flash error message
        return render_template('Admin/view_courses.html')

# Manage users


@admin_dashboard_app.route('/view_users')
def view_users():
    try:
        mycursor.execute("SELECT * FROM user WHERE name != 'admin'")
        users = mycursor.fetchall()

        # Search functionality
        search_term = request.args.get('search_term')
        if search_term:
            filtered_users = [user for user in users if search_term.lower(
            ) in user[1].lower() or search_term.lower() in user[4].lower()]
            users = filtered_users

        # Sorting functionality
        sort_by = request.args.get('sort_by')
        if sort_by:
            if sort_by == 'name':
                users.sort(key=lambda x: x[1])
            elif sort_by == 'country':
                users.sort(key=lambda x: x[4])

        return render_template('Admin/view_users.html', users=users, user_count=len(users), search_term=search_term)
    except mysql.connector.Error as err:
        flash(f"An error occurred: {err}", 'error')  # Flash error message
        return render_template('Admin/view_users.html')


@admin_dashboard_app.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    try:
        sql = "DELETE FROM User WHERE id = %s"
        mycursor.execute(sql, (user_id,))
        mydb.commit()

        mycursor.execute("SELECT * FROM user WHERE name != 'admin'")
        users = mycursor.fetchall()
        flash(
            f"User with ID {user_id} has been deleted successfully!", "success")
        return render_template('Admin/view_users.html', users=users)
    except mysql.connector.Error as err:
        flash(f"An error occurred: {err}", "error")
        return render_template('Admin/view_users.html')


if __name__ == '__main__':
    app.register_blueprint(admin_dashboard_app)
    app.run(debug=True)
