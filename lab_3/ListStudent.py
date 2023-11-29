from students import Student

class StudentList:
    def __init__(self):
        self.students = []

    def Studentadd(self, student):
        #self.students.append(student)
        if self.students == []:
            self.students.append(student)
        else:
            insertPosition = 0 
            for st in self.students:
                if student.name > st.name:
                    insertPosition += 1
                else:
                    break
            self.students.insert(insertPosition, student)
                
    def Studentremove(self, name):
        self.students = [s for s in self.students if s.name != name]

    def StudentUpd(self, name, new_name, new_surname, new_age, new_phone):
        for student in self.students:
            if student.name == name:
                student.name = new_name
                student.surname = new_surname
                student.age = new_age
                student.phone = new_phone

    def __str__(self):
        return '\n'.join(str(student) for student in self.students)

