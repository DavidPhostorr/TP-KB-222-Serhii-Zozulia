class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Studetns name is {self.name} Mark {self.age}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,age):
        if age < 0:
            raise ValueError("Age should be more then 0")
        self._age = age
        
def NewStudent():
    try:
        name = input('Enter student name: ')
        age = int(input('Enter student age: '))
        student = Student(name,age)
    except Exception as e:
        print(e)
        return NewStudent()
    else:
        return student
        
def main():
    count = int(input('Count of student: '))
    student = []
    for _ in range(count):
        student.append(NewStudent())
    for student in sorted(student, key=lambda s: s.age):
        print(student) 
        
main()