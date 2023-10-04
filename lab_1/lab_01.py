
## List [Item1, Item2, Item3]
## Item {"name":"Jon", "phone":"0631234567"}

# already sorted list
list = [
    {"name":"Bob", "surname": "Bobchenko", "age" : "17", "phone":"0631234567"},
    {"name":"Emma", "surname": "Emchenko", "age" : "18", "phone":"0631234567"},
    {"name":"Jon", "surname": "Jonchenko", "age" : "16", "phone":"0631234567"},
    {"name":"Zak", "surname": "Zakchenko", "age" : "19", "phone":"0631234567"}
]

def printAllList():
    sorted_list = sorted(list, key=lambda x: x["name"])
    for elem in sorted_list:
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
    # find insert position
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
    name1 = input("Enter new name: ")
    surname = input("Enter new surname: ")
    age = input("Enter new age: ")
    phone = input("Enter new phone: ")
    newElement = {"name": name1, "surname" : surname, "age" : age, "phone": phone}
    updateElem = -1
    for item in list:
        if name == item["name"]:
            updateElem = list.index(item)
            break
    if updateElem == -1:
        print("Element was not found")
    else:
        print("Update" + str(updateElem))
    list[updateElem] = newElement
     
     

            
            

    

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
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
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Leaving...")
                break
            case _:
                print("Wrong chouse")


main()