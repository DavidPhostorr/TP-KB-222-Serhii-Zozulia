try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(e)


dict = {"a": 1, "b": 2}
try:
    value = dict["c"]
except KeyError as e:
    print(e)

try:
    num = 5 + "10"
except TypeError as e:
    print(e)
