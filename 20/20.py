import numpy as np
import re
from functools import reduce
from collections import Counter

#Finds the intersection between two lists
def intersection(l1, l2):
    temp = set(l2)
    l3 = [value for value in l1 if value in temp]
    return l3

#Finds the possible sea monsters in an image
#It does this by basically searching in three lines for each specific part of the monster and looking if any of these regexes line up in their span
def findSeaMonsters(image):
    #The regexes are strange because it is using a lookahead to not actually capture the parts and to get all possibilities
    topRegex = r"(?=(..................#.))"
    midRegex = r"(?=(#....##....##....###))"
    bottomRegex = r"(?=(.#..#..#..#..#..#...))"
    count = 0
    for i in range(1, len(image)-1, 1):
        #Grabs the span of the regex for each match in all possible matches
        topMatches = [x.span() for x in re.finditer(topRegex, image[i-1])]
        midMatches = [x.span() for x in re.finditer(midRegex, image[i])]
        bottomMatches = [x.span() for x in re.finditer(bottomRegex, image[i+1])]
        if topMatches != [] and midMatches != [] and bottomMatches != []:
            #Gets the intersections of these three regexes so basically places they all span together
            count += len(reduce(intersection, [topMatches, midMatches, bottomMatches]))
    return count

#Rotates an image using numpy
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

#Flips an image using numpy
def flip(image, direction):
    newImage = np.array(image)
    if direction == 1:
        #Flip on x-axis (Horizontal)
        newImage = np.flipud(newImage)
    else:
        #Flip on y-axis (Vertical)
        newImage = np.fliplr(newImage)
    return newImage.tolist()

#Finds the border that would be touching the direction we are searching for
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

#Finds the image that will match the current image we have
#Does this by checking every possible transformation of every possible remaining image and seeing if any of the edges fit together
#Yes its a bruteforce
def findMatch(image, direction, tiles):
    foundIndex = -1
    foundImage = -1
    #Grab the border we care about matching up based on the direction we are trying to match
    if direction == "n":
        border = image[0]
    elif direction == "s":
        border = image[-1]
    elif direction == "e":
        border = [x[-1] for x in image]
    elif direction == "w":
        border = [x[0] for x in image]
    
    #For every tile we are going to try every possible rotation/flip/combo/standard and see if any of the edges match up
    for i in range(len(tiles)):
        if foundIndex != -1:
            break
        tile = tiles[i][0]
        #There are 100% repeated images in this sequence but it works and doesn't really effect performance so cleanup can wait
        possibleTiles = [tile, flip(tile,0), flip(tile,1), rotate(tile, "cw", 1), rotate(tile, "cw", 2), rotate(tile, "cw", 3), rotate(tile, "ccw", 1), rotate(tile, "ccw", 2), rotate(tile, "ccw", 3), flip(rotate(tile, "cw", 1),1), flip(rotate(tile, "cw", 1),0), flip(rotate(tile, "ccw", 1),1), flip(rotate(tile, "ccw", 1),0)]
        for option in possibleTiles:
            if border == newBorder(option, direction):
                #Once we found the image break out of all this
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

#Makes the grid way bigger than it has to be so it doesn't matter what starting image we drop where and since its all empty its not wasting really any space
finalImage = [[[] for _ in range(2*len(tiles))] for _ in range(2*len(tiles))]
temp = [[] for _ in range(2*len(tiles))]
#We are starting in the middle of the big grid we have so it can grow fully in any direction
i = j = len(tiles)
#Put the first tile in there and remove it from the list
newTiles = [(i,j)]
finalImage[i][j] = tiles.pop(0)

#Now for every new tile we find we add it to this list to eventually search for its neighbors
for tile in newTiles:
    i = tile[0]
    j = tile[1]
    image = finalImage[i][j][0]
    #Check if its neighbors are empty or not and if they are then we try to find a match
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


#This messy loop just gets rid of everything that is empty, so both empty rows and empty cells in occupied rows
finalImage = [[y for y in x if y != []] for x in finalImage if x != temp]
#Multiply the 4 corner ID's together
print(finalImage[0][0][1] * finalImage[0][-1][1] * finalImage[-1][0][1] * finalImage[-1][-1][1])

#### PART 2
cleanImage = []
#Get the cleaned image, aka get rid of the borders and cell ID's
for line in finalImage:
    cleanLine = []
    for cell in line:
        newCell = cell[0][1:-1]
        newCell = newCell[::-1]
        newCell = [x[1:-1] for x in newCell]
        cleanLine.append(newCell)
    cleanImage.append(cleanLine)

#Combine rows across images together so we wind up with just big rows
fullCleanImage = []
for line in cleanImage:
    for i in range(len(line[0])):
        fullLine = []
        for image in line:
            fullLine.extend(image[i])
        fullCleanImage.append(fullLine)

#Again try every possible combo of flips and rotations
possibleImages = [fullCleanImage, flip(fullCleanImage,0), flip(fullCleanImage,1), rotate(fullCleanImage, "cw", 1), rotate(fullCleanImage, "cw", 2), rotate(fullCleanImage, "cw", 3), rotate(fullCleanImage, "ccw", 1), rotate(fullCleanImage, "ccw", 2), rotate(fullCleanImage, "ccw", 3), flip(rotate(fullCleanImage, "cw", 1),1), flip(rotate(fullCleanImage, "cw", 1),0), flip(rotate(fullCleanImage, "ccw", 1),1), flip(rotate(fullCleanImage, "ccw", 1),0)]
counts = []
#For every image try to find the sea monsters in them
for image in possibleImages:
    joinedImage = ["".join(x) for x in image]
    counts.append(findSeaMonsters(joinedImage))
seaMonsters = max(counts)

#A sea monster is made of 15 #'s
#Get every # and then subtract the number that make up the sea monsters
total = sum([Counter(list(x))["#"] for x in fullCleanImage])
print(total - (seaMonsters * 15))
