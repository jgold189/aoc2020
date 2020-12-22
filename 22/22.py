import copy

def playGame(P1, P2):
    p1 = copy.deepcopy(P1)
    p2 = copy.deepcopy(P2)
    history = set()
    while len(p1) > 0 and len(p2) > 0:
        #Some junk to make it so you can hash on these two lists by converting them both to full strings
        tempString = ",".join([str(x) for x in p1]) + ":" + ",".join([str(x) for x in p2])
        if tempString in history:
            return (p1,p2,1)
        else:
            history.add(tempString)
        p1Card = p1.pop(0)
        p2Card = p2.pop(0)
        #If we have enough cards
        if p1Card <= len(p1) and p2Card <= len(p2):
            #We recurse
            subP1, subP2, flag = playGame(p1[:p1Card], p2[:p2Card])
            if len(subP1) > len(subP2) or flag:
                p1.append(p1Card)
                p1.append(p2Card)
            else:
                p2.append(p2Card)
                p2.append(p1Card)
        else:
            #Play normally
            if p1Card > p2Card:
                p1.append(p1Card)
                p1.append(p2Card)
            else:
                p2.append(p2Card)
                p2.append(p1Card)
    return (p1,p2,0)

fin = open("input.txt", "r")
data = [x.strip() for x in fin.readlines()]

p1 = [int(x) for x in data[1:data.index("")]]
p2 = [int(x) for x in data[data.index("")+2:]]

p1, p2, flag = playGame(p1, p2)

winner = p1 if len(p1) > len(p2) or flag else p2
winner.reverse()
points = 0
for i in range(len(winner)):
    points += winner[i] * (i + 1)
print(points)
