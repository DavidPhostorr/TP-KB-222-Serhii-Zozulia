# update()

dict = {'a' : 'bi', 'b' : 'bs', 'c' : 'bo', 'd' : 'a'}
dict1 = {'b' : 'ba', 'd' : 'ba'}

dict.update(dict1)

print(dict)

# del

dict2 = {'a' : 'bi', 'b' : 'ba', 'c' : 'sd'}
del dict2['c']

print(dict2)

# clear

dict3 = {'a' : 'bi', 'b' : 'ba'}
dict3.clear()

print(dict3)

# keys()

dict4 = {'a': 'bi', 'b': 'ba', 'c': 'bo', 'd': 'ba'}
k = dict4.keys()

print(k)

# values()

dict5 = {'a': 'bi', 'b': 'ba', 'c': 'bo', 'd': 'ba'}
v = dict5.values()

print(v)

# items()

dict6 = {'a': 'bi', 'b': 'ba', 'c': 'bo', 'd': 'ba'}
i = dict6.items()

print(i)
