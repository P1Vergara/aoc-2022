import string

lowerCaseValues = dict()
upperCaseValues = dict()
totalPoints = 0

def setupLetterValues():
    for index, letter in enumerate(string.ascii_lowercase):
       lowerCaseValues[letter] = index + 1

    for index, letter in enumerate(string.ascii_uppercase):
        upperCaseValues[letter] = index + 27

def findLetterValue(letter):
    global totalPoints
    
    if (letter.isupper()):
        if letter in upperCaseValues:
            totalPoints += upperCaseValues[letter]
    else:
        if letter in lowerCaseValues:
            totalPoints += lowerCaseValues[letter]

def searchBadge(group):
    # find same letters between first and second sack letters
    letters = []
    for x in group[0]:
        index = group[1].find(x)

        if (index != -1):
            letters.append(group[1][index])
    
    # find same letters between the first found letters
    # and the third sack letters
    otherLetters = []
    for l in letters:
        index = group[2].find(l)

        if (index != -1):
            otherLetters.append(group[2][index])
    
    # return the first ocurrence of a similar letter
    # on the three sacks of letters
    # print(otherLetters)
    return otherLetters[0]

def lookInGroups(groups):
    badge = ''
    for group in groups:
        print(len(group))
        badge = searchBadge(group)
        findLetterValue(badge)
    
def readInput():
    with open('/Users/p1vergara/Desktop/AOC-2022/day-03/input.txt') as input:
        groups = []
        group = []
        counter = 1

        for line in input.readlines():
            if (counter < 3):
                group.append(line.strip())
                counter += 1
            else:
                group.append(line.strip())
                groups.append(group)
                group = []
                counter = 1

        lookInGroups(groups)
        
    
setupLetterValues()
readInput()

print('-------RESULT-------')
print(totalPoints)
print('--------------------')