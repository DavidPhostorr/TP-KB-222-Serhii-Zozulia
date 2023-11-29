class Student:
    def __init__(self, name,surname,age,phone):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
    def __str__(self):
        return f"Student name is {self.name}, Student surname is {self.surname}, Student age is {self.age}, Phone is {self.phone}"