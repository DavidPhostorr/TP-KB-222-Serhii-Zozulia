from operation import *
from function import *


while True:
    print("Choose:")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Devide")
    print("5. Exit")
    
    choiсe = input("Enter operation nubmer: ")
    
    if choiсe == "5":
        print("Leaving...")
        break
    
    if choiсe in ('1','2','3','4'):
        
        n1 = GetIntValue("Enter first number: ")
        n2 = GetIntValue("Enter second number: ")

        
        if choiсe == '1':
            result = add(n1,n2)  
            print("Result: ", +result)
        elif choiсe == '2':
            result = subtract(n1,n2)
            print("Result: ", +result)
        elif choiсe == '3':
            result = multiply(n1,n2)
            print("Result: ", +result)
        elif choiсe == '4':
            result = divide(n1,n2)
            print("Result: ", result)
        else:
            result = "Incorrect"
            print("Incorrect ")
    
    logs(choiсe,n1,n2,result)