# aX**2 + bX + c = 0
# D = b**2 - 4ac

# x1 = (-b + sqrt(D))/2*a
# x2 = (-b - sqrt(D))/2*a
import math

a = int(input("a : "))
b = int(input("b: "))
c = int(input("c: "))


def findD(a, b ,c):

    d = b**2 - 4*a*c
    return d

result = findD(a, b, c)

print(findD(a, b, c))