import csv

def loadData(fname):
    data = []
    with open(fname, 'r') as file:
        csvread = csv.reader(file)
        for row in csvread:
            data.append(row)
    return data

def savedata(fname, data):
    with open(fname, 'w' , newline='') as file:
        csvwr = csv.writer(file)
        csvwr.writerows(data)
        
fname = 'lab2.csv'
ldata = loadData(fname)
print(ldata)        