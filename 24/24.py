import re

def countBlack(tiles):
    count = 0
    for key in tiles:
        if tiles[key]:
            count += 1
    return count

def checkNeighbors(x,y):
    count = 0
    for neighbor in calcNeighbors(x,y):
        try:
            if tiles[neighbor]:
                count += 1
        except KeyError:
            pass
    return count

def calcNeighbors(x,y):
    neighbors = [(x-1,y), (x+1,y), (x-.5,y-1), (x+.5,y-1), (x-.5,y+1), (x+.5,y+1)]
    return neighbors


fin = open("input.txt", "r")
data = [x.strip() for x in fin.readlines()]
ROUNDS = 100

instructions = []
regex = r"ne|se|nw|sw|e|w"
for line in data:
    fullInstruct = []
    groups = re.finditer(regex, line)
    for group in groups:
        fullInstruct.append(group[0])
    instructions.append(fullInstruct)

tiles = {}
for instruct in instructions:
    x = 0
    y = 0
    for command in instruct:
        if command == "e":
            x += 1
        elif command == "w":
            x -= 1
        elif command == "ne":
            y += 1
            x += 0.5
        elif command == "nw":
            y += 1
            x -= 0.5
        elif command == "se":
            y -= 1
            x += 0.5
        elif command == "sw":
            y -= 1
            x -= 0.5
    #True is black, false is white
    tiles[(x,y)] = not tiles[(x,y)] if (x,y) in tiles else True
    for neighbor in calcNeighbors(x,y):
        tiles[neighbor] = tiles[neighbor] if neighbor in tiles else False

for _ in range(ROUNDS):
    newTiles = {}
    for key in tiles:
        neighbors = checkNeighbors(*key)
        if tiles[key]:
            #Tile is currently black
            if neighbors == 0 or neighbors > 2:
                newTiles[key] = False
            else:
                newTiles[key] = True
        else:
            #Tile is currently white
            if neighbors == 2:
                newTiles[key] = True
                for neighbor in calcNeighbors(*key):
                    newTiles[neighbor] = newTiles[neighbor] if neighbor in newTiles else False
            else:
                newTiles[key] = False
    tiles = newTiles

print(countBlack(tiles))