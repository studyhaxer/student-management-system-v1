def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
def get_non_empty(prompt):
    while True:
        user_inpt = input(prompt)
        if(len(user_inpt.strip()) > 0):
            return user_inpt
        else:
            print("Please enter valid input.")
def display_student(student):
    print("-" * 40)
    print(f"ID      : {student.id}")
    print(f"Name    : {student.name}")
    print(f"Age     : {student.age}")
    print(f"Course  : {student.course}")
    print(f"Marks   : {student.marks}")
    print("-" * 40)