# config.py
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'adminroot@123'
MYSQL_DB = 'fluentfusion'

'''
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL
);

CREATE TABLE course (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id)
);

CREATE TABLE teacher (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    teacher_name VARCHAR(255),
    qualification VARCHAR(255),
    major_subject VARCHAR(255),
    ratings FLOAT
);

ALTER TABLE course ADD FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id);
'''
