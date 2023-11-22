from students import Student
from ListStudent import StudentList
from Utils import Utils

def main():
    student_list = StudentList()

    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, E exec, S save, X exit] ")

        match choice:
            case "C" | "c":
                print("New element will be created:")
                name = input("Please enter student name: ")
                surname = input("Please enter student surname: ")
                age = input("Please enter student age: ")
                phone = input("Please enter student phone: ")
                student = Student(name, surname, age, phone)
                student_list.Studentadd(student)
                print("New element has been added")

            case "U" | "u":
                print("Existing element will be updated")
                name = input("Please enter name to be updated: ")
                new_name = input("Enter new name: ")
                new_surname = input("Enter new surname: ")
                new_age = input("Enter new age: ")
                new_phone = input("Enter new phone: ")
                student_list.StudentUpd(name, new_name, new_surname, new_age, new_phone)
            case "D" | "d":
                print("Element will be deleted")
                name = input("Please enter name to be deleted: ")
                student_list.Studentremove(name)

            case "P" | "p":
                print("List will be printed")
                print(student_list)

            case "E" | "e":
                file_csv = input("Enter CSV file name: ")
                Utils.addCSV(file_csv, student_list.students)

            case "S" | "s":
                file_csv = input("Enter name of CSV file: ")
                Utils.saveCSV(file_csv, student_list.students)

            case "X" | "x":
                print("Leaving...")
                break

            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()
