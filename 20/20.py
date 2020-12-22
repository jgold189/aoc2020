import numpy as np
import re
from functools import reduce
from collections import Counter

def intersection(l1, l2):
    temp = set(l2)
    l3 = [value for value in l1 if value in temp]
    return l3

def findSeaMonsters(image):
    topRegex = r"(?=(..................#.))"
    midRegex = r"(?=(#....##....##....###))"
    bottomRegex = r"(?=(.#..#..#..#..#..#...))"
    count = 0
    for i in range(1, len(image)-1, 1):
        topMatches = [x.span() for x in re.finditer(topRegex, image[i-1])]
        midMatches = [x.span() for x in re.finditer(midRegex, image[i])]
        bottomMatches = [x.span() for x in re.finditer(bottomRegex, image[i+1])]
        if topMatches != [] and midMatches != [] and bottomMatches != []:
            count += len(reduce(intersection, [topMatches, midMatches, bottomMatches]))
    return count

def rotate(image, direction, times):
    newImage = np.array(image)
    if direction == "cw":
        #Rotate clockwise
        axes = (1,0)
    else:
        #Rotate counterclockwise
        axes = (0,1)
    newImage = np.rot90(newImage,times,axes)
    return newImage.tolist()

def flip(image, direction):
    newImage = np.array(image)
    if direction == 1:
        #Flip on x-axis (Horizontal)
        newImage = np.flipud(newImage)
    else:
        #Flip on y-axis (Vertical)
        newImage = np.fliplr(newImage)
    return newImage.tolist()

def newBorder(image, direction):
    if direction == "s":
        border = image[0]
    elif direction == "n":
        border = image[-1]
    elif direction == "w":
        border = [x[-1] for x in image]
    elif direction == "e":
        border = [x[0] for x in image]
    return border

def findMatch(image, direction, tiles):
    foundIndex = -1
    foundImage = -1
    if direction == "n":
        border = image[0]
    elif direction == "s":
        border = image[-1]
    elif direction == "e":
        border = [x[-1] for x in image]
    elif direction == "w":
        border = [x[0] for x in image]
    
    for i in range(len(tiles)):
        if foundIndex != -1:
            break
        tile = tiles[i][0]
        #There are 100% repeated images in this sequence but it works and doesn't really effect performance so cleanup can wait
        possibleTiles = [tile, flip(tile,0), flip(tile,1), rotate(tile, "cw", 1), rotate(tile, "cw", 2), rotate(tile, "cw", 3), rotate(tile, "ccw", 1), rotate(tile, "ccw", 2), rotate(tile, "ccw", 3), flip(rotate(tile, "cw", 1),1), flip(rotate(tile, "cw", 1),0), flip(rotate(tile, "ccw", 1),1), flip(rotate(tile, "ccw", 1),0)]
        #for option in possibleTiles:
        #    pprint(option)
        #sys.exit(-1)
        for option in possibleTiles:
            if border == newBorder(option, direction):
                foundIndex = i
                foundImage = (option, tiles[i][1])
                break

    return (foundIndex, foundImage)



fin = open("input.txt", "r")
data = [x.strip() for x in fin.readlines()]

#Input handling
tiles = []
image = []
for line in data:
    if "Tile" in line:
        number = int(line.split(" ")[1][:-1])
    elif line == "":
        tiles.append((image, number))
        image = []
    else:
        image.append(list(line))
tiles.append((image, number))


finalImage = [[[] for _ in range(2*len(tiles))] for _ in range(2*len(tiles))]
temp = [[] for _ in range(2*len(tiles))]
i = j = len(tiles)
newTiles = [(i,j)]
finalImage[i][j] = tiles.pop(0)

for tile in newTiles:
    i = tile[0]
    j = tile[1]
    image = finalImage[i][j][0]
    if finalImage[i+1][j] == []:
        #North
        matchIndex, matchImage = findMatch(image, "n", tiles)
        if matchIndex != -1:
            finalImage[i+1][j] = matchImage
            newTiles.append((i+1,j))
            tiles.pop(matchIndex)
    if finalImage[i-1][j] == []:
        #South
        matchIndex, matchImage = findMatch(image, "s", tiles)
        if matchIndex != -1:
            finalImage[i-1][j] = matchImage
            newTiles.append((i-1,j))
            tiles.pop(matchIndex)
    if finalImage[i][j+1] == []:
        #East
        matchIndex, matchImage = findMatch(image, "e", tiles)
        if matchIndex != -1:
            finalImage[i][j+1] = matchImage
            newTiles.append((i,j+1))
            tiles.pop(matchIndex)
    if finalImage[i][j-1] == []:
        #West
        matchIndex, matchImage = findMatch(image, "w", tiles)
        if matchIndex != -1:
            finalImage[i][j-1] = matchImage
            newTiles.append((i,j-1))
            tiles.pop(matchIndex)



finalImage = [[y for y in x if y != []] for x in finalImage if x != temp]
print(finalImage[0][0][1] * finalImage[0][-1][1] * finalImage[-1][0][1] * finalImage[-1][-1][1])

#### PART 2
cleanImage = []
for line in finalImage:
    cleanLine = []
    for cell in line:
        newCell = cell[0][1:-1]
        newCell = newCell[::-1]
        newCell = [x[1:-1] for x in newCell]
        cleanLine.append(newCell)
    cleanImage.append(cleanLine)

fullCleanImage = []
for line in cleanImage:
    for i in range(len(line[0])):
        fullLine = []
        for image in line:
            fullLine.extend(image[i])
        fullCleanImage.append(fullLine)

possibleImages = [fullCleanImage, flip(fullCleanImage,0), flip(fullCleanImage,1), rotate(fullCleanImage, "cw", 1), rotate(fullCleanImage, "cw", 2), rotate(fullCleanImage, "cw", 3), rotate(fullCleanImage, "ccw", 1), rotate(fullCleanImage, "ccw", 2), rotate(fullCleanImage, "ccw", 3), flip(rotate(fullCleanImage, "cw", 1),1), flip(rotate(fullCleanImage, "cw", 1),0), flip(rotate(fullCleanImage, "ccw", 1),1), flip(rotate(fullCleanImage, "ccw", 1),0)]
counts = []
for image in possibleImages:
    joinedImage = ["".join(x) for x in image]
    counts.append(findSeaMonsters(joinedImage))
seaMonsters = max(counts)

#A sea monster is made of 15 #'s
total = sum([Counter(list(x))["#"] for x in fullCleanImage])
print(total - (seaMonsters * 15))
