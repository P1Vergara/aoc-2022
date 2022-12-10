containers = []
instructions = []
containersLoaded = False

def moveContainers(targets, origin, dest):
    # move a container for each pending target
    # on the instruction
    pendingTargets = targets
    tempContainer = ''
    
    while pendingTargets > 0:
        # find the original container and then
        # save it in a temp var, after that replace the
        # original container with a space string

        originTargetFound = False
        originRow = 0

        while not originTargetFound:
            if (containers[originRow][origin] == ' '):
                originRow += 1
            else:
                tempContainer = containers[originRow][origin]
                containers[originRow][origin] = ' '

                originTargetFound = True
        
        # check if we run out of rows to check
        # for empty spaces, if thats the case
        # add a new row of empty spaces and reset
        # the search
        destTargetFound = False
        destRow = len(containers) - 1

        while destTargetFound == False:
            if (destRow >= 0):
                # look for the first empty space in the colunmn
                # from bottom to top,
                if (containers[destRow][dest] == ' '):
                    containers[destRow][dest] = tempContainer
                    destTargetFound = True
                else:
                    destRow -= 1
            else:
                # hard coded empty row because I'm super lazy
                containers.insert(0, [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
                destRow = len(containers) - 1
            
        pendingTargets -= 1


def readInstructions():
    for inst in instructions:
        targets = int(inst.split(' ')[1])
        origin = int(inst.split(' ')[3]) - 1
        dest = int(inst.split(' ')[5]) - 1

        moveContainers(targets, origin, dest)


def splitContainersFromInstructions(line):
    global containersLoaded, containers, instructions

    if (containersLoaded == False):
        counter = 0
        row = []
        
        for char in line[0]:
            if counter == 1:
                if (char == '' and (char != '[' or char != ']')):
                    row.append('')
                else:
                    row.append(char)
                counter += 1
            elif (counter == 4):
                counter = 0
                counter += 1
            else:
                counter += 1
        
        containers.append(row)
    else:
        instructions.append(line[0])


def readInput():
    global containersLoaded

    with open('/Users/p1vergara/Desktop/AOC-2022/day-05/input.txt') as input:
        for line in input.readlines():
            # check if the line is the gap between containers
            # and instruction
            if (len(line.splitlines()[0].strip()) == 0):
                containersLoaded = True
                continue
            
            splitContainersFromInstructions(line.splitlines())
        
    containers.pop()


readInput()
readInstructions()

print('-------RESULT-------')
for x in containers:
    print(x)
print('--------------------')