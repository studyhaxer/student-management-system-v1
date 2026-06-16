# 🎓 Student Management System V1

A command-line Student Management System built with Python and SQLite — created as part of my **#60DaysOfPython** challenge on **Day 10**.

---

## 📋 Features

- ➕ Add a new student
- 📋 View all students
- 🔍 Search student by ID
- ✏️ Update student record
- 🗑️ Delete student record
- 🏆 View top scorer
- 📊 View average marks

---

## 🗂️ Project Structure

```
Student_Management_System_V1/
│
├── main.py          # Entry point, menu navigation
├── database.py      # DB connection and table creation
├── student_crud.py  # CRUD operations
├── models.py        # Student class
├── utils.py         # Input validation and display helpers
├── config.py        # App configuration (DB name, App title)
└── .gitignore       # Ignores pycache and .db files
```

---

## 🛠️ Technologies Used

- Python 3
- SQLite3 (built-in)

---

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/studyhaxer/student-management-system-v1.git
```

2. Navigate to the project folder:
```bash
cd student-management-system-v1
```

3. Run the app:
```bash
python main.py
```

> No external libraries required!

---

## 📚 What I Learned

- Connecting and working with SQLite in Python
- Writing and executing SQL queries (CRUD)
- Separating concerns across multiple files
- Input validation with loops and exceptions
- Using classes and `__str__` for clean data modeling

---

## 👨‍💻 Author

**studyhaxer** — Day 10 of #60DaysOfPython 🐍
