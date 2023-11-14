import csv

list = [
    {"name":"Bob", "surname": "Bobchenko", "age" : "17", "phone":"0631234567"},
    {"name":"Emma", "surname": "Emchenko", "age" : "18", "phone":"0631234567"},
    {"name":"Jon", "surname": "Jonchenko", "age" : "16", "phone":"0631234567"},
    {"name":"Zak", "surname": "Zakchenko", "age" : "19", "phone":"0631234567"}
]

def printAllList():
    for elem in list:
        if isinstance(elem, dict):
            strForPrint = "Student name is " + elem["name"] + ",  Student surname is " + elem["surname"] + ",  Student age is " + elem["age"] + ",  Phone is " + elem["phone"]
            print(strForPrint)
        else:
            print("Not a student in list:", elem)
    return


def addNewElement():
    name = input("Pease enter student name: ")
    surname = input("Please enter student surname: ")
    age = input("Please enter student age: ")
    phone = input("Please enter student phone: ")
    
    newItem = {"name": name, "surname" : surname, "age" : age, "phone": phone}
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        # list.pop(deletePosition)
        del list[deletePosition]
    return


def updateElement():
    name = input("Please enter name to be updated: ")
    for index, elem in enumerate(list):
        if name == elem["name"]:
            name1 = input("Enter new name: ")
            surname = input("Enter new surname: ")
            age = input("Enter new age: ")
            phone = input("Enter new phone: ")
            newElement = {"name": name1, "surname" : surname, "age" : age, "phone": phone}
            del list[index]
            insertPos = 0
            for pos, elem in enumerate(list):
                if name1 > elem["name"]:
                    insertPos = pos + 1
                else:
                    break
            list.insert(insertPos, newElement)
            print("Element has been updated")
            break
        else:
            print("Student not found")
     
def addCSV(fname):
    try:
        with open(fname, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                list.append(row)
        print("Data loaded succesfully")
    except FileNotFoundError:
        print("File mot found")
    except Exception as e:
        print(f"An error occurred: {e}")

def saveCSV(fname):
    try:
        with open(fname, 'w', newline='') as file:
            fieldnames = ["name", "surname", "age", "phone"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for item in list:
                writer.writerow(item)
        print("Data saved successfully")
    except Exception as e:
        print(f"An error occurred: {e}")
            
            

    

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print, E exec, S save, X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "E" | "e":
                fileCSV = input("Enter CSV file name: ")
                addCSV(fileCSV)
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Leaving...")
                break
            case "S" | "s":
                FileCSV = input("Enter name of CSV file: ")
                saveCSV(FileCSV)
            case _:
                print("Wrong chouse")


main()