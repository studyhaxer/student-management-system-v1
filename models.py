class Student:
    def __init__(self, id, name, age, course, marks):
        self.id = id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def __str__(self):
        return f'({self.id}, {self.name}, {self.age}, {self.course}, {self.marks})'

    @classmethod
    def from_row(cls, row):
        return cls(*row)