while True:
    print("Choose:")
    print("1. Add")
    print("2. Exit")
    
    choiсe = input("Enter operation nubmer: ")
    
    if choiсe == "2":
        print("Leaving...")
        break
    
    if choiсe in ('1'):
        
        if choiсe == '1':
            n1 = float(input("Enter number: "))
            n2 = float(input("Enter a number: "))
            n3 = n1 + n2
            print("Result: ", +n3 )