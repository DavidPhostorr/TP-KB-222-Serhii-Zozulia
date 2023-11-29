import unittest
from students import Student
from ListStudent import StudentList

class TestStudentList(unittest.TestCase):

    def setUp(self):
        self.student_list = StudentList()

    def test_add_student(self):
        student = Student("John", "Doe", 25, "123456789")
        self.student_list.Studentadd(student)
        
        self.assertIn(student, self.student_list.students)
        self.assertEqual(len(self.student_list.students), 1)

    def test_remove_student(self):
        student = Student("John", "Doe", 25, "123456789")
        self.student_list.Studentadd(student)

        self.student_list.Studentremove("John")
        self.assertNotIn(student, self.student_list.students)
        self.assertEqual(len(self.student_list.students), 0)

    def test_update_student(self):
        student = Student("John", "Doe", 25, "123456789")
        self.student_list.Studentadd(student)

        self.student_list.StudentUpd("John", "Jane", "Smith", 30, "987654321")
        updated_student = self.student_list.students[0]

        self.assertEqual(updated_student.name, "Jane")
        self.assertEqual(updated_student.surname, "Smith")
        self.assertEqual(updated_student.age, 30)
        self.assertEqual(updated_student.phone, "987654321")

    def test_str_representation(self):
        student1 = Student("Jane", "Doe", 25, "123456789")
        student2 = Student("John", "Smith", 30, "987654321")

        self.student_list.Studentadd(student1)
        self.student_list.Studentadd(student2)

        expected_output = "Student name is Jane, Student surname is Smith, Student age is 30, Phone is 987654321\n" \
                          "Student name is John, Student surname is Doe, Student age is 25, Phone is 123456789"
        self.assertEqual(str(self.student_list), expected_output)

if __name__ == '__main__':
    unittest.main()
