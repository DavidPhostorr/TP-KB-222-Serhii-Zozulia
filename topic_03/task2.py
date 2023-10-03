# extend()

list = ['bi' , 'ba']
list1 = ['bo' , 'ba']

list.extend(list1)

print(list)

# append()

list2 = ['biba']
list2.append('boba')

print(list2)

# insert(id, val)

list3 = ['bi', 'ba', 'ba']
list3.insert(2, 'bo')

print(list3)

# remove(val)

list4 = ['bi', 'ba', 'bo', 'ba' , 'bu']
list4.remove('bu')

print(list4)

# clear()

list5 = ['bi', 'ba']
list5.clear()

print(list5)

# sort()

list6 = ['2bo', '4bi' , '3ba', '1ba' ]
list6.sort(reverse=True)

print(list6)

# reverse()

list7 = ['ba', 'bo' , 'ba', 'bi' ]
list7.reverse()

print(list7)

# copy()

list8 = ['bi' , 'ba' , 'bo' , 'ba']
list9 = list8.copy()

print(list9)