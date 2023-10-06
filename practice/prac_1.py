def findMinElemWithIndex(listForSearch):
    if not listForSearch:
        return -1, None
    
    elem = listForSearch[0]
    id = 0
    
    for i in range(1, len(listForSearch)):
        if listForSearch[i] < elem:
            elem = listForSearch[i]
            id = i

    return id, elem

def findMaxElemWithIndex(listForSearch):
    if not listForSearch:
        return -1, None
    elem = listForSearch[0]
    id = 0
    
    for i in range(1, len(listForSearch)):
        if listForSearch[i] > elem:
            elem = listForSearch[i]
            id = i
    
    return id, elem

def main():
    listOfData = [11, 14, 22, 33, 7, 88, 123, 345, 64, 10, 5, 55, 66, 44, 20]
    
    result = findMinElemWithIndex(listOfData)
    print(f"Min id: {result[0]}, Min value: {result[1]}")

    result = findMaxElemWithIndex(listOfData)
    print(f"Max id: {result[0]}, Max value: {result[1]}")

if __name__ == "__main__":
    main()
