import csv
from lab_2 import printAllList,addNewElement,deleteElement,updateElement,addCSV,saveCSV

students_list = []

def test_printAllList():
    students_list.append({"name": "John", "surname": "Doe", "age": "20", "phone": "123456789"})
    assert printAllList() == "Student name is John,  Student surname is Doe,  Student age is 20,  Phone is 123456789"
    students_list.clear()

def test_addNewElement():
    addNewElement("John", "Doe", "20", "123456789")
    assert students_list == [{"name": "John", "surname": "Doe", "age": "20", "phone": "123456789"}]

def test_deleteElement():
    students_list.append({"name": "John", "surname": "Doe", "age": "20", "phone": "123456789"})
    deleteElement("John")
    assert students_list == []

def test_updateElement():
    students_list.append({"name": "John", "surname": "Doe", "age": "20", "phone": "123456789"})
    updateElement("John", "Jane", "Doe", "20", "123456789")
    assert students_list == [{"name": "Jane", "surname": "Doe", "age": "20", "phone": "123456789"}]

def test_addCSV():
    addCSV("test.csv")
    assert students_list == [{"name": "Jane", "surname": "Doe", "age": "20", "phone": "123456789"}]

def test_saveCSV():
    saveCSV("test.csv")
    with open("test.csv", 'r') as file:
        reader = csv.DictReader(file)
        assert list(reader) == [{"name": "Jane", "surname": "Doe", "age": "20", "phone": "123456789"}]
        
