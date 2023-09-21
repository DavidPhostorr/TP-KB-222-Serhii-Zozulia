def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Impossible"
    return x / y

while True:
    print("Choose:")
    print("1. Add = '+' ")
    print("2. Substract = '-' ")
    print("3. Multiply = '*' ")
    print("4. Devide = '/' ")
    print("5. Exit = ']'")
     
    operation = input('Enter operation sign: ')
    
    if operation == "]":
        print("Leaving...")
        break
    else: 
    
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        match operation:
    
            case '+':
                print(add(x,y))
            case '-':
                print(subtract(x, y))
            case '*':
                print(multiply(x, y))
            case '/':
                print(divide(x, y))
            case ']':
                print(' ')
            case _:
                print("Invalid operation")