fin = open("input.txt", "r")

data = fin.readlines()

oldCorrectPass = 0
newCorrectPass = 0
for line in data:
    prop, passw = line.strip().split(":")
    num, letter = prop.split(" ")
    minNum, maxNum = num.split("-")
    minNum = int(minNum)
    maxNum = int(maxNum)
    oldCount = 0
    for char in passw:
        if char == letter:
            oldCount += 1
    if oldCount >= minNum and oldCount <= maxNum:
        oldCorrectPass += 1

    if (passw.strip()[minNum-1] == letter) != (passw.strip()[maxNum-1] == letter):
        newCorrectPass += 1
    
print("Old Correct Passwords:", oldCorrectPass)
print("New Correct Passwords:", newCorrectPass)