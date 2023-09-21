import math

def findD(a,b,c):
    d = b**2 - 4*a*c
    return d    

def findR(a,b,c):
    d = findD(a,b,c)
    
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1,x2
    elif d == 0:
        x1 = -b / (2* a)
        return x1
    else:
        return None
a = int(input("a : "))
b = int(input("b: "))
c = int(input("c: "))

R = findR(a,b,c)
if R is not None:
    x1, x2 = R
    if x1 and x2 is not None:
        print("Firs root: " +str(x1))
        print("Second root:" +str(x2))
    elif x1 is None:
        print("First root: " +str(x1))
        print("Second root not found")
    elif x2 is None:
        print("First root not found")
        print("Second root is: " +str(x2))
    else: 
        print("Roots not found")
                

     