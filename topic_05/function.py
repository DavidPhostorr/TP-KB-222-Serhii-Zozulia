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