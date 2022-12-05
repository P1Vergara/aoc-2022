cals = []
threeMaxCals = []
currentCal = 0

def sumCalories(cal):
    global cals, currentCal
    print(cal)
    
    if (cal.strip()):
        if (cal != ''):
            currentCal += int(cal)
        else:
            cals.append(currentCal)
    else:
        cals.append(currentCal)
        currentCal = 0

def findThreeMaxValues():
    global cals, threeMaxCals

    for a in range(3):
        threeMaxCals.append(max(cals))
        cals.remove(max(cals))
    
    sum = 0
    for x in threeMaxCals:
        sum += x
    
    return sum

def readInput():
    with open('/Users/p1vergara/Desktop/AOC-2022/day-01/input.txt') as input:
        for line in input.readlines():
            sumCalories(line)

        # send an empty line it's just a way to finish the count
        sumCalories('') 

        print('-------RESULT-------')
        print(findThreeMaxValues())
        print('--------------------')
    
readInput()