from flask import Blueprint, render_template, request, flash, session
import mysql.connector

# Create a Blueprint for this route
user_dashboard_app = Blueprint('user_dashboard', __name__)

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


# @user_dashboard_app.route('/user')
# def user_dash():
#     return render_template('user/user_dash.html')


@user_dashboard_app.route('/change_pass', methods=['GET', 'POST'])
def change_password():
    if request.method == 'POST':
        current_password = request.form['current_password']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        mycursor.execute(
            "SELECT * FROM user WHERE password = %s", (current_password,))
        user = mycursor.fetchone()

        # Add validation for the new password
        if new_password != confirm_password:
            flash('New password and confirm password do not match!', 'error')
        elif len(new_password) < 8:
            flash('Password should be at least 8 characters long.', 'error')
        else:
            try:
                # Assuming you have stored the user ID in the session
                session.clear()
                session['id'] = user[0]
                user_id = session['id']
                print(user_id)
                mycursor.execute(
                    "SELECT password FROM user WHERE id = %s", (user_id,))
                row = mycursor.fetchone()
                print("----->>>>")
                print(row[0])
                if row and row[0] == current_password:
                    sql = "UPDATE user SET password = %s WHERE id = %s"
                    mycursor.execute(sql, (new_password, user_id))
                    mydb.commit()
                    flash('Password changed successfully!', 'success')
                else:
                    flash('Incorrect current password. Please try again.', 'error')
            except mysql.connector.Error as err:
                flash(f"An error occurred: {err}", 'error')
    return render_template('user/change_password.html')


@user_dashboard_app.route('/courses')
def courses():
    return render_template('user/courses.html')


@user_dashboard_app.route('/view_courses')
def view_courses():
    try:
        mycursor.execute("SELECT * FROM course")
        courses = mycursor.fetchall()
        print(courses)
        return render_template('user/courses.html', courses=courses)
    except mysql.connector.Error as err:
        flash(f"An error occurred: {err}", 'error')  # Flash error message
        return render_template('user/courses.html')


@user_dashboard_app.route('/reg_courses')
def reg_courses():
    return render_template('user/reg_courses.html')


user_data = {}


@user_dashboard_app.route('/profile')
def profile():
    try:
        # Fetch the user ID using the correct key
        user_id = session.get('id', None)
        print(user_id)
        if user_id:
            mycursor.execute(
                "SELECT name, email, country FROM user WHERE id = %s", (user_id,))
            user = mycursor.fetchall()
            # print("\n--->")
            # print(user)
            if user:
                return render_template('User/profile.html', user=user)
            else:
                flash('User not found', 'error')
                return render_template('User/profile.html')
        else:
            flash('User not logged in', 'error')
            return render_template('User/profile.html')
    except mysql.connector.Error as err:
        flash(f"An error occurred: {err}", 'error')
        return render_template('User/profile.html')


if __name__ == '__main__':
    app.run(debug=True)
