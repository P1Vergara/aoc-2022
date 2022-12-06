import math
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


def findRepeatedItems(first, second):
    letter = ''
    for x in first:
        index = second.find(x)
        if (index != -1):
            letter = second[index]

            findLetterValue(letter)
            break

def splitCompartments(sack):
    sackContent = sack.strip()
    sackLength = len(sackContent)
    sackHalf = math.floor(sackLength / 2)

    first = sackContent[0 : sackHalf]
    second = sackContent[sackHalf : sackLength]

    findRepeatedItems(first, second)

def readInput():
    with open('/Users/p1vergara/Desktop/AOC-2022/day-03/input.txt') as input:
        for line in input.readlines():
            splitCompartments(line)

setupLetterValues()
readInput()

print('-------RESULT-------')
print(totalPoints)
print('--------------------')