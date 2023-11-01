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
        Operation = operation()
        Function = function()
        n1 = Function.GetIntValue("Enter first number: ")
        n2 = Function.GetIntValue("Enter second number: ")

        
        if choiсe == '1':
            result = Operation.add(n1,n2)  
            print("Result: ", +result)
        elif choiсe == '2':
            result = Operation.subtract(n1,n2)
            print("Result: ", +result)
        elif choiсe == '3':
            result = Operation.multiply(n1,n2)
            print("Result: ", +result)
        elif choiсe == '4':
            result = Operation.divide(n1,n2)
            print("Result: ", result)
        else:
            result = "Incorrect"
            print("Incorrect ")
    
    Function.logs(choiсe,n1,n2,result)