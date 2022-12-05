totalPoints = 0

def sumPoints(round):
    global totalPoints

    splitted = round.split()

    elfChoice = checkForElfChoice(splitted[0])
    winState = checkForWinState(splitted[1])
    myChoice = ''
    myPoints = 0

    # check what result I want
    match(winState['state']):
        case 'WIN':
            myPoints += winState['points']

            if (elfChoice == 'ROCK'):
                myPoints += 2
                myChoice = 'PAPER'
            elif (elfChoice == 'PAPER'):
                myPoints += 3
                myChoice = 'SCISSOR'
            else:
                myPoints += 1
                myChoice = 'PAPER'
        case 'LOSE':
            myPoints += winState['points']

            if (elfChoice == 'ROCK'):
                myPoints += 3
                myChoice = 'SCISSOR'
            elif (elfChoice == 'PAPER'):
                myPoints += 1
                myChoice = 'ROCK'
            else:
                myPoints += 2
                myChoice = 'PAPER'
        case 'DRAW':
            myPoints += winState['points']
            myChoice = elfChoice

            if (myChoice == 'ROCK'):
                myPoints += 1
            elif (myChoice == 'PAPER'):
                myPoints += 2
            else:
                myPoints += 3
    
    totalPoints += myPoints
    
def checkForWinState(param):
    winState = ''
    points = 0
    match(param):
        case 'Y':
            winState = 'DRAW'
            points = 3
        case 'X':
            winState = 'LOSE'
            points = 0
        case 'Z':
            winState = 'WIN'
            points = 6
    return {'state': winState, 'points': points}

def checkForElfChoice(param):
    choice = ''
    match(param):
        case 'A':
            choice = 'ROCK'
        case 'B':
            choice = 'PAPER'
        case 'C':
            choice = 'SCISSOR'
    return choice

def readInput():
    with open('/Users/p1vergara/Desktop/AOC-2022/day-02/input.txt') as input:
        for line in input.readlines():
            sumPoints(line)
    
    print('-------RESULT-------')
    print(totalPoints)
    print('--------------------')
    
readInput()