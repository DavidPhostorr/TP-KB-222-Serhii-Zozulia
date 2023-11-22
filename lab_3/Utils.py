import csv
from students import Student

class Utils:
    @staticmethod
    def addCSV(fname, data_list):
        try:
            with open(fname, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(row['name'], row['surname'], row['age'], row['phone'])
                    data_list.append(student)
            print("Data loaded successfully")
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    @staticmethod
    def saveCSV(fname, students):
        try:
            with open(fname, 'w', newline='') as file:
                fieldnames = ["name", "surname", "age", "phone"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for student in students:
                    writer.writerow({"name": student.name, "surname": student.surname, "age": student.age, "phone": student.phone})
            print("Data saved successfully")
        except Exception as e:
            print(f"An error occurred: {e}")