import copy

def checkNeighborsP1(x, y, data):
    maxX = len(data[0])
    maxY = len(data)
    neighbors = 0
    nCoords = [(0,1), (1,0), (1,1), (0,-1), (-1,0), (-1,-1), (-1,1), (1,-1)]
    for coord in nCoords:
        newX = x + coord[1]
        newY = y + coord[0]
        if newX >= 0 and newX < maxX and newY >= 0 and newY < maxY:
            n = data[newY][newX]
            neighbors += 1 if n == "#" else 0
    return neighbors

def checkNeighborsP2(x, y, data):
    maxX = len(data[0])
    maxY = len(data)
    neighbors = 0
    nCoords = [(0,1), (1,0), (1,1), (0,-1), (-1,0), (-1,-1), (-1,1), (1,-1)]
    for coord in nCoords:
        isFloor = True
        newX = x + coord[1]
        newY = y + coord[0]
        while isFloor:
            isFloor = False
            if newX >= 0 and newX < maxX and newY >= 0 and newY < maxY:
                n = data[newY][newX]
                if n == "#":
                    neighbors += 1
                elif n == ".":
                    newX += coord[1]
                    newY += coord[0]
                    isFloor = True
    return neighbors



fin = open("input.txt", "r")
newData = list(map(lambda x: list(x.strip()), fin.readlines()))

oldData = []
oldOccuCount = -1
newOccuCount = 0
while oldOccuCount != newOccuCount:
    oldOccuCount = newOccuCount
    oldData = copy.deepcopy(newData)
    for y in range(len(oldData)):
        for x in range(len(oldData[0])):
            if oldData[y][x] != ".":
                #Part 1
                #neighbors = checkNeighborsP1(x, y, oldData)
                neighbors = checkNeighborsP2(x, y, oldData)
                if oldData[y][x] == "L" and neighbors == 0:
                    newData[y][x] = "#"
                #Part 1
                #elif oldData[y][x] == "#" and neighbors >= 4:
                elif oldData[y][x] == "#" and neighbors >= 5:
                    newData[y][x] = "L"
    newOccuCount = sum(x.count("#") for x in newData)
    print(newOccuCount)
print(newOccuCount)
