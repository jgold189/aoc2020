#Part 2 is gonna be done in a silly way because I want to mess around with generators in Python, probably better just to sort and see what is missing

import math

#Just a simple generator
def generateSeat(x):
    num = x + 1
    while True:
        yield num
        num += 1

def passToSeat(bpass):
    minRow = 0
    maxRow = 127
    minCol = 0
    maxCol = 7
    for char in bpass:
        if char == "F":
            maxRow -= math.ceil((maxRow - minRow) / 2)
        elif char == "B":
            minRow = math.ceil((maxRow + minRow) / 2)
        elif char == "L":
            maxCol -= math.ceil((maxCol - minCol) / 2)
        elif char == "R":
            minCol = math.ceil((minCol + maxCol) / 2)

    #minRow and maxRow are the same at this point, same with col
    return ((minRow * 8) + minCol) 

fin = open("input.txt", "r")
data = list(map(lambda x: x.strip(), fin.readlines()))

seatIDList = list(map(passToSeat, data))

lowestSeatID = min(seatIDList)
highestSeatID = max(seatIDList)

print(highestSeatID)

seatGen = generateSeat(lowestSeatID)
missingSeat = 0
while missingSeat == 0:
    seat = next(seatGen)
    if seat not in seatIDList:
        missingSeat = seat

print(missingSeat)