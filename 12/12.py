import re

def moveShip(shipX, shipY, wayX, wayY, val):
    for _ in range(val):
        shipX += wayX
        shipY += wayY
    return((shipX, shipY))

def moveWaypoint(x, y, dir, val):
    if dir == "N":
        return((x, y+val))
    elif dir == "S":
        return((x, y-val))
    elif dir == "E":
        return((x+val, y))
    elif dir == "W":
        return((x-val, y))
    raise Exception("Invalid Direction passed to moveShip")

def turnWaypoint(wayX, wayY, dir, val):
    if dir == "L":
        if val == 90:
            newX = wayY * -1
            newY = wayX
        elif val == 180:
            newX = wayX * -1
            newY = wayY * -1
        elif val == 270:
            newX = wayY
            newY = wayX * -1
    else:
        if val == 90:
            newX = wayY
            newY = wayX * -1
        elif val == 180:
            newX = wayX * -1
            newY = wayY * -1
        elif val == 270:
            newX = wayY * -1
            newY = wayX
    return((newX,newY))

#### PART 1
#def turnShip(dir, val, facing):
#    dirToDegrees = {"N": 0, "E": 90, "S": 180, "W": 270}
#    degreesToDir = {0: "N", 90: "E", 180: "S", 270: "W"}
#    if dir == "L" and val != 180:
#        return degreesToDir[(((dirToDegrees[facing] + val) % 360) + 180) % 360]
#    else:
#        return degreesToDir[(dirToDegrees[facing] + val) % 360]


fin = open("input.txt", "r")
data = list(map(lambda x: x.strip(), fin.readlines()))

regex = r"^([A-Z])([0-9]+)"
shipX = 0
shipY = 0
wayX = 10
wayY = 1
facing = "E"
for instruct in data:
    command = re.match(regex, instruct)
    if command.group(1) == "F":
        shipX,shipY = moveShip(shipX, shipY, wayX, wayY, int(command.group(2)))
    elif command.group(1) == "L" or command.group(1) == "R":
        #facing = turnShip(command.group(1), int(command.group(2)), facing)
        wayX,wayY = turnWaypoint(wayX, wayY, command.group(1), int(command.group(2)))
    else:
        wayX,wayY = moveWaypoint(wayX, wayY, command.group(1), int(command.group(2)))
print(abs(shipX) + abs(shipY))