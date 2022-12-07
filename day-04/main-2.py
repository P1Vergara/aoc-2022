total = 0

def checkRanges(A1, A2, B1, B2):
    global total

    if(A1 >= B1 and A1 <= B2 ):
        total += 1
    elif(A2 <= B2 and A2 >= B1):
        total += 1
    elif(B2 >= A1 and B2 <= A2):
        total += 1
    elif(B1 >= A1 and B1 <= A2):
        total += 1
    
def splitRanges(line):
    first = line.split(',')[0]
    second = line.split(',')[1]

    firstStart = int(first.split('-')[0])
    firstEnd = int(first.split('-')[1])
    secondStart = int(second.split('-')[0])
    secondEnd = int(second.split('-')[1])

    checkRanges(firstStart, firstEnd, secondStart, secondEnd)

def readInput():
    with open('/Users/p1vergara/Desktop/AOC-2022/day-04/input.txt') as input:
        for line in input.readlines():
            splitRanges(line.strip())

readInput()

print('-------RESULT-------')
print(total)
print('--------------------')