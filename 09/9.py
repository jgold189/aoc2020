def validNumber(num, last25):
    for value in last25:
        if (num - value) in last25 and (num - value) != value:
            return True
    return False

fin = open("input.txt", "r")
data = list(map(lambda x: int(x.strip()), fin.readlines()))

last25 = data[0:25]
invalidNum = -1
for i in range(25, len(data), 1):
    currentNum = data[i]
    if validNumber(currentNum, last25):
        last25.append(currentNum)
        last25.pop(0)
    else:
        invalidNum = currentNum
        break
print(invalidNum)

startPos = 0
endPos = 2
while startPos < len(data):
    currentSum = sum(data[startPos:endPos])
    if currentSum == invalidNum:
        print(min(data[startPos:endPos]) + max(data[startPos:endPos]))
        break
    elif currentSum > invalidNum:
        startPos += 1
        endPos = startPos + 2
    else:
        endPos += 1