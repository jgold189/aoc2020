#Wasn't implemented great. Lotta hardcoding that should be removed

#Linked list and dict of all cups to objects
class node():
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


fin = open("input.txt", "r")
data = [x.strip() for x in fin.readlines()]

ROUNDS = 10000000
cupList = [int(x) for x in data[0]]
for i in range(len(cupList)+1, 1000001):
    cupList.append(i)
cupLen = len(cupList)
cupDict = {}
for i in range(cupLen):
    currentCup = node(cupList[i])
    cupDict[currentCup.value] = currentCup
    if i > 0:
        cupDict[cupList[i-1]].next = currentCup
cupDict[cupList[-1]].next = cupDict[cupList[0]]

currentCup = cupDict[cupList[0]]
for _ in range(ROUNDS):
    pickupCup = currentCup.next
    nextCup = currentCup.next
    pickedUp = set()
    pickedUp.add(nextCup.value)
    for i in range(2):
        nextCup = nextCup.next
        pickedUp.add(nextCup.value)
    currentCup.next = nextCup.next

    lookingFor = currentCup.value - 1 if currentCup.value > 1 else cupLen
    while lookingFor in pickedUp:
        if lookingFor == 1:
            lookingFor = cupLen
        else:
            lookingFor -= 1
        
    oldNext = cupDict[lookingFor].next
    cupDict[lookingFor].next = pickupCup
    nextCup = pickupCup.next
    nextCup = nextCup.next
    nextCup.next = oldNext

    currentCup = currentCup.next

#### PART 1
#cup = cupDict[1].next
#while cup.value != 1:
#    print(cup.value, end="")
#    cup = cup.next

#### PART 2
print(cupDict[1].next.value * cupDict[1].next.next.value)
