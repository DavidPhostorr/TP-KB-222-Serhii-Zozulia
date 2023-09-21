import math 

def sqrt(x):
    return math.sqrt(x)

def pow(x, y):
    return math.pow(x, y)

def log(x):
    return math.log(x)

def log10(x):
    return math.log10(x)

while True:
    print("Choose:")
    print("1. Sqrt")
    print("2. Pow")
    print("3. Log")
    print("4. Log10")
    print("5. Exit")
    
    choiсe = input("Enter operation nubmer: ")
    
    if choiсe == "5":
        print("Leaving...")
        break
    
    if choiсe in ('1','2','3','4'):
        
        if choiсe == '1':
            n1 = float(input("Enter number: "))
            print("Result: ", sqrt(n1))
        elif choiсe == '2':
            n1 = float(input("Enter first number: "))
            n2 = float(input("Enter second number: "))
            print("Result: ", pow(n1,n2))
        elif choiсe == '3':
            n1 = float(input("Enter logarifm : "))
            print("Result: ", log(n1))
        elif choiсe == '4':
            n1 = float(input("Enter log10: "))
            print("Result: ", log10(n1))
        else: 
            print("Incorrect ")