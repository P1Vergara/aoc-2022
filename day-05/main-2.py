containers = []
instructions = []
containersLoaded = False

def moveContainers(targets, origin, dest):
    # move a container for each pending target
    # on the instruction
    tempContainers = []
    originTargetsFound = False
    originRow = 0
    destTargetsFound = False
    destRow = len(containers) - 1
    pendingTargets = targets

    # find all origin containers
    # save them in a temp container
    while not originTargetsFound:
        while pendingTargets > 0:
            if (containers[originRow][origin] == ' '):
                originRow += 1
            else:
                tempContainers.append(containers[originRow][origin])
                containers[originRow][origin] = ' '
                originRow += 1
                pendingTargets -= 1

        originTargetsFound = True
    
    # find all destination containers
    while destTargetsFound == False:
        # here we save the temp container on their destination
        # until we have save every container we dont stop this loop
        while len(tempContainers) > 0:
            if (destRow >= 0):
                # look for the first empty space in the colunmn
                # from bottom to top,
                if (containers[destRow][dest] == ' '):
                    containers[destRow][dest] = tempContainers.pop()
                    destRow -= 1
                else:
                    destRow -= 1
            else:
                # hard coded empty row because I'm super lazy
                containers.insert(0, [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
                destRow = len(containers) - 1
        
        destTargetsFound = True


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