def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return ZeroDivisionError(x,y)

def ZeroDivisionError(x, y):
    while True:
        try:
            if x == 0 or y == 0:
                return "Impossible"
        except ZeroDivisionError:
            print("Impossible")

def GetIntValue(promt):
    while True:
        try:
            x = float(input(promt))
            return x
        except ValueError:
            print("Value error")

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
            print("Result: ", add(n1,n2))
        elif choiсe == '2':
            print("Result: ", subtract(n1,n2))
        elif choiсe == '3':
            print("Result: ", multiply(n1,n2))
        elif choiсe == '4':
            print("Result: ", divide(n1,n2))
        else: 
            print("Incorrect ")
    

