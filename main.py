from database import create_table
import student_crud
import utils
from config import APP_TITLE
def addstudent():
    name = utils.get_non_empty("Enter Student Name: ")
    age = utils.get_int("Enter Student Age: ")
    course = utils.get_non_empty("Enter Student Course: ")
    marks = utils.get_float("Enter Student marks: ")
    msg = student_crud.add_student(name,age,course,marks)
    print(msg)
def viewstudents():
    students = student_crud.get_all_students()
    if not students:
        print("No students found. ")
        return
    for student in students:
        utils.display_student(student)
def getstudentbyid():
    student_id = utils.get_int("Enter Student Id: ")
    student = student_crud.get_student_by_id(student_id)
    if student:
        utils.display_student(student)
    else:
        print("No student found with that Id. ")
def gettopscorer():
    student = student_crud.get_top_scorer()
    if student:
        utils.display_student(student)
    else:
        print("No student Exist. ")
def getaveragemarks():
    student = student_crud.get_average_marks()
    if student:
        print(f"Average Marks: {student[0]}")
    else:
        print("No student Exist. ")
def updatestudent():
    student_id = utils.get_int("Enter Student Id: ")
    name = utils.get_non_empty("Enter Student Name: ")
    age = utils.get_int("Enter Student Age: ")
    course = utils.get_non_empty("Enter Student Course: ")
    marks = utils.get_float("Enter Student marks: ")
    msg = student_crud.update_student(student_id,name,age,course,marks)
    print(msg)
def deletestudent():
    student_id = utils.get_int("Enter Student Id: ")
    response = utils.get_non_empty("Are you Sure Y/N?")
    if(response == 'Y'):
        msg = student_crud.delete_student(student_id)
        print(msg)    
    else:
        print("Action Aborted. ")
def show_menu():
    create_table()
    while True:
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Top Scorer")
        print("7. Average Marks")
        print("8. Exit")
        choice = utils.get_int("Please Enter Value Between 1 to 8: ")
        if choice == 1:
            addstudent()
        elif choice == 2:
            viewstudents()
        elif choice == 3:
            getstudentbyid()
        elif choice == 4:
            updatestudent()
        elif choice == 5:
            deletestudent()
        elif choice == 6:
            gettopscorer()
        elif choice == 7:
            getaveragemarks()
        elif choice == 8:
            exit()
        else:
            print("Invalid Choice. ")
def main():
    show_menu()
if __name__ == "__main__":
    main()