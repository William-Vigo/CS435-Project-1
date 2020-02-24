import random

def getRandomArray(n):
    randList = []
    while(len(randList) < n):
        randNum = random.randint(0,n*n)
        if(randNum not in randList):
            randList.append(randNum)
    return randList

def getSortedArray(n):
    sorted = []
    for i in range(n, 0, -1):
        sorted.append(i)
    return sorted

#Problem 3a
print(getRandomArray(10))

#Problem 3b
print(getSortedArray(10))

