# Import necessary libraries
from flask import redirect, url_for
import mysql.connector
from flask import Flask, render_template, request, flash, Blueprint, session

# Create a Blueprint for this route
admin_dashboard_app = Blueprint('admin_dashboard', __name__)

# Create a Flask app instance
app = Flask(__name__)
app.secret_key = 'fluentfusionsuccess'  # Add your own secret key

# Configure the MySQL connection
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'adminroot@123'
MYSQL_DB = 'fluentfusion'

# Establish a connection to the MySQL database
mydb = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DB
)

# Create a cursor object for database operations
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


@admin_dashboard_app.route('/update_course_page/<int:course_id>', methods=['GET'])
def update_course_page(course_id):
    try:
        mycursor.execute(
            "SELECT * FROM course WHERE course_id=%s", (course_id,))
        course = mycursor.fetchone()
        if course:
            return render_template('Admin/update_course.html', courses=course)
        else:
            flash('Course not found', 'error')
            return render_template('Admin/view_courses.html')
    except mysql.connector.Error as err:
        flash(f"An error occurred: {err}", 'error')
        return render_template('Admin/view_courses.html')


@admin_dashboard_app.route('/update_course/<int:course_id>', methods=['POST'])
def update_course(course_id):
    try:
        title = request.form['title']
        description = request.form['description']
        teacher_id = request.form['teacher_id']

        mycursor = mydb.cursor()
        sql = "UPDATE course SET title=%s, description=%s, teacher_id=%s WHERE course_id=%s"
        val = (title, description, teacher_id, course_id)
        mycursor.execute(sql, val)
        mydb.commit()

        mycursor.execute("SELECT * FROM course")
        courses = mycursor.fetchall()
        mycursor.close()

        flash("Course updated successfully!", 'success')
        return render_template('Admin/view_courses.html', courses=courses)

    except Exception as e:
        flash(f"An error occurred: {e}", 'error')  # Flash error message
        return render_template('Admin/view_courses.html')


@admin_dashboard_app.route('/view_course')
def view_course():
    try:
        mycursor.execute("SELECT * FROM course")
        courses = mycursor.fetchall()
        print(courses)
        return render_template('Admin/view_courses.html', courses=courses)
    except mysql.connector.Error as err:
        flash(f"An error occurred: {err}", 'error')  # Flash error message
        return render_template('Admin/view_courses.html')


@admin_dashboard_app.route('/delete_course/<int:course_id>', methods=['POST'])
def delete_course(course_id):
    try:
        sql = "DELETE FROM course WHERE course_id = %s"
        mycursor.execute(sql, (course_id,))
        mydb.commit()

        mycursor.execute("SELECT * FROM course")
        courses = mycursor.fetchall()
        flash(
            f"Course with ID {course_id} has been deleted successfully!", "success")
        return render_template('Admin/view_courses.html', courses=courses)
    except mysql.connector.Error as err:
        flash(f"An error occurred: {err}", "error")
        return render_template('Admin/view_courses.html')

# Manage users ------------------>


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

# Manage teachers------------------------>


@admin_dashboard_app.route('/manage_teachers')
def manage_teachers():
    return render_template('Admin/manage_teachers.html')


@admin_dashboard_app.route('/add_teacher', methods=['GET', 'POST'])
def add_teacher():
    if request.method == 'POST':
        try:
            teacher_name = request.form['teacher_name']
            qualification = request.form['qualification']
            major_subject = request.form['major_subject']
            ratings = request.form['ratings']

            mycursor = mydb.cursor()
            sql = "INSERT INTO teacher (teacher_name, qualification, major_subject, ratings) VALUES (%s, %s, %s, %s)"
            val = (teacher_name, qualification, major_subject, ratings)
            mycursor.execute(sql, val)
            mydb.commit()

            mycursor.execute("SELECT * FROM teacher")
            teachers = mycursor.fetchall()
            print(teachers)

            mycursor.close()
            flash("Teacher added successfully!", 'success')
            return render_template('Admin/view_teach.html', teachers=teachers)
        except mysql.connector.Error as err:
            flash(f"An error occurred: {err}", 'error')  # Flash error message
            return render_template('Admin/manage_teachers.html')
    else:
        return render_template('Admin/add_teachers.html')


@admin_dashboard_app.route('/view_teachers')
def view_teachers():
    try:
        mycursor.execute("SELECT * FROM teacher")
        teachers = mycursor.fetchall()
        print(teachers)
        return render_template('Admin/view_teach.html', teachers=teachers)
    except mysql.connector.Error as err:
        flash(f"An error occurred: {err}", 'error')  # Flash error message
        return render_template('Admin/view_teach.html')


@admin_dashboard_app.route('/update_teacher_page/<int:teacher_id>', methods=['GET'])
def update_teacher_page(teacher_id):
    try:
        mycursor.execute(
            "SELECT * FROM teacher WHERE teacher_id=%s", (teacher_id,))
        teacher = mycursor.fetchone()
        if teacher:
            return render_template('Admin/update_teacher.html', teacher=teacher)
        else:
            flash('Teacher not found', 'error')
            return render_template('Admin/view_teachers.html')
    except mysql.connector.Error as err:
        flash(f"An error occurred: {err}", 'error')
        return render_template('Admin/view_teachers.html')


@admin_dashboard_app.route('/update_teacher/<int:teacher_id>', methods=['POST'])
def update_teacher(teacher_id):
    try:
        teacher_name = request.form['teacher_name']
        qualification = request.form['qualification']
        major_subject = request.form['major_subject']
        ratings = request.form['ratings']

        mycursor = mydb.cursor()
        sql = "UPDATE teacher SET teacher_name=%s, qualification=%s, major_subject=%s, ratings=%s WHERE teacher_id=%s"
        val = (teacher_name, qualification, major_subject, ratings, teacher_id)
        mycursor.execute(sql, val)
        mydb.commit()

        mycursor.execute("SELECT * FROM teacher")
        teachers = mycursor.fetchall()
        mycursor.close()

        flash("Teacher updated successfully!", 'success')
        return render_template('Admin/view_teach.html', teachers=teachers)

    except Exception as e:
        flash(f"An error occurred: {e}", 'error')  # Flash error message
        return render_template('Admin/view_teach.html')


@admin_dashboard_app.route('/delete_teacher/<int:teacher_id>', methods=['POST'])
def delete_teacher(teacher_id):
    try:
        sql = "DELETE FROM teacher WHERE teacher_id = %s"
        mycursor.execute(sql, (teacher_id,))
        mydb.commit()

        mycursor.execute("SELECT * FROM teacher")
        teachers = mycursor.fetchall()
        flash(
            f"Teacher with ID {teacher_id} has been deleted successfully!", "success")
        return render_template('Admin/view_teach.html', teachers=teachers)
    except mysql.connector.Error as err:
        flash(f"An error occurred: {err}", "error")
        return render_template('Admin/view_teach.html')


if __name__ == '__main__':
    app.register_blueprint(admin_dashboard_app)
    app.run(debug=True)
