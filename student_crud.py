import sqlite3
import database
from models import Student
def add_student(name, age, course, marks):
    conn = database.get_connection()
    cursor = conn.cursor()
    try:
        stdnt_qry = """INSERT INTO students (name, age, course, marks) VALUES (?, ?, ?, ?)"""
        cursor.execute(stdnt_qry, (name, age, course, marks))
        conn.commit()
        msg = "Student Added Successfully. "
    except sqlite3.Error as error:
        msg = f"Error occurred - {error}"
    conn.close()
    return msg
def get_all_students():
    conn = database.get_connection()
    cursor = conn.cursor() 
    qry = """select * from students"""
    cursor.execute(qry)
    data = cursor.fetchall()
    conn.close()
    return [Student.from_row(row) for row in data]
def get_student_by_id(student_id):
    conn = database.get_connection()
    cursor = conn.cursor()
    search_qry =  ("""SELECT * FROM students WHERE id = ?""")
    cursor.execute(search_qry, (student_id,))
    row = cursor.fetchone()    
    conn.close()
    if row:
        return Student.from_row(row)
    return None
def get_top_scorer():
    conn = database.get_connection()
    cursor = conn.cursor()
    query = """SELECT * FROM students ORDER BY marks DESC LIMIT 1"""
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    if row:
        return Student.from_row(row)
    return None
def get_average_marks():
    conn = database.get_connection()
    cursor = conn.cursor()
    query = """SELECT AVG(marks) FROM students"""
    cursor.execute(query)
    avg = cursor.fetchone()
    conn.close()
    if avg:
        return avg
    return None
def update_student(student_id, name, age, course, marks):
    conn = database.get_connection()
    cursor = conn.cursor()
    try:
        updt_qry = ("""UPDATE students SET name=?, age=?,course=?, marks=? WHERE id=?""")
        cursor.execute(updt_qry, (name,age,course,marks,student_id))
        if cursor.rowcount == 1:
            msg= "Record Updted Successfully. "
        else:
            msg = "Student doest not exist against this Id. "
    except sqlite3.Error as error:
        msg = f"Error occurred - {error}"
    conn.commit()
    conn.close()
    return msg
def delete_student(student_id):
    conn = database.get_connection()
    cursor = conn.cursor()
    try:
        del_qry = ("""DELETE FROM students WHERE id = ?""")
        cursor.execute(del_qry,(student_id,))
        if cursor.rowcount == 1:
            msg ="Record Deleted Successfully. "
        else:
            msg = "Student does not exist against this Id. "
    except sqlite3.Error as error:
        msg = f"Error occurred - {error}"
    conn.commit()
    conn.close()
    return msg
    

   