def lookForMarker(signalSplits, fullSignal):
    for signal in signalSplits:
        # change signal to a set object, this trims duplicate
        # characters, if the length is different then there are duplicates
        hasDuplicates = len(set(signal)) != len(signal)
        
        # once we find the duplicate we look for the signal
        # marker inside the full signal, then we add the length of
        # the marker to get the start-of-packet marker
        if (not hasDuplicates):
            print(fullSignal.find(signal) + 4)
            break
    

def readSignal(line):
    signalsRead = False
    signalSplits = []
    signal = ''
    lineLength = len(line)
    start = 0
    end = 4

    while not signalsRead:
        # stop reading signals if we reach the end
        if (end >= lineLength):
            signalsRead = True
        
        signal = line[start : end]
        signalSplits.append(signal)
        signal = ''

        start += 1
        end += 1
    
    lookForMarker(signalSplits, line)

def readInput():
    with open('/Users/p1vergara/Desktop/AOC-2022/day-06/input.txt') as input:
        for line in input.readlines():
            readSignal(line.strip())

readInput()

print('-------RESULT-------')
print('--------------------')