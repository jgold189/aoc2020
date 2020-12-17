# This is the 4th dimension version, it was just a small modification from the 3 dimensional version

import copy

def countNeighbors(key, cubes):
    activeNeighbors = 0
    newCoords = []
    x,y,z,w = [int(a) for a in key.split(",")]
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            for k in range(z-1, z+2):
                for l in range(w-1, w+2):
                    coord = str(i) + "," + str(j) + "," + str(k) + "," + str(l)
                    if coord != key:
                        if coord in cubes:
                            if cubes[coord] == "#":
                                activeNeighbors += 1
                        else:
                            newCoords.append(coord)
    return (activeNeighbors,newCoords)



fin = open("input.txt", "r")
data = [list(x.strip()) for x in fin.readlines()]

cycles = 6
cubes = {}
for y in range(len(data)):
    for x in range(len(data[y])):
        coords = str(x) + "," + str(y) + ",0,0"
        cubes[coords] = data[y][x]
for y in range(-1, len(data)+1):
    for x in range(-1, len(data[0])+1):
        for z in range(-1, 2):
            for w in range(-1, 2):
                coords = str(x) + "," + str(y) + "," + str(z) + "," + str(w)
                if coords not in cubes:
                    cubes[coords] = "."

newCubes = {}
for _ in range(cycles):
    #print(sum([1 if cubes[key] == "#" else 0 for key in cubes]))
    for key in cubes:
        activeNeighbors,newCoords = countNeighbors(key, cubes)
        if activeNeighbors > 0:
            for coord in newCoords:
                newCubes[coord] = "."
        if (activeNeighbors == 2 or activeNeighbors == 3) and cubes[key] == "#":
            newCubes[key] = "#"
        elif activeNeighbors == 3 and cubes[key] == ".":
            newCubes[key] = "#"
        else:
            newCubes[key] = "."
    cubes = copy.deepcopy(newCubes)
    newCubes = {}
print(sum([1 if cubes[key] == "#" else 0 for key in cubes]))
