totalPoints = 0

def sumPoints(round):
    global totalPoints

    splitted = round.split()

    elfChoice = checkForElfChoice(splitted[0])
    myChoice = checkForMyChoice(splitted[1])

    match(myChoice):
        case 'ROCK':
            totalPoints += 1

            match(elfChoice):
                case 'ROCK':
                    totalPoints += 3
                case 'PAPER':
                    totalPoints += 0
                case 'SCISSORS':
                    totalPoints += 6  
        case 'PAPER':
            totalPoints += 2

            match(elfChoice):
                case 'ROCK':
                    totalPoints += 6
                case 'PAPER':
                    totalPoints += 3
                case 'SCISSORS':
                    totalPoints += 0
        case 'SCISSORS':
            totalPoints += 3

            match(elfChoice):
                case 'ROCK':
                    totalPoints += 0
                case 'PAPER':
                    totalPoints += 6
                case 'SCISSORS':
                    totalPoints += 3
    
def checkForMyChoice(param):
    choice = ''
    match(param):
        case 'Y':
            choice = 'PAPER'
        case 'X':
            choice = 'ROCK'
        case 'Z':
            choice = 'SCISSORS'
    return choice

def checkForElfChoice(param):
    choice = ''
    match(param):
        case 'A':
            choice = 'ROCK'
        case 'B':
            choice = 'PAPER'
        case 'C':
            choice = 'SCISSORS'
    return choice


def readInput():
    with open('/Users/p1vergara/Desktop/AOC-2022/day-02/input.txt') as input:
        for line in input.readlines():
            sumPoints(line)
    
    print('-------RESULT-------')
    print(totalPoints)
    print('--------------------')

readInput()


