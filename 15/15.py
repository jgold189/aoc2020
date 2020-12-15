fin = open("input.txt", "r")
#New parsing method after testing. I miss map already.
data = [int(x.strip()) for x in fin.readlines()[0].split(",")]

PART1 = 2020
PART2 = 30000000
i = 1
numbers = {}
for num in data[0:-1]:
    numbers[num] = i
    i += 1
lastNum = data[-1]
lasti = i
i += 1
while i <= PART2:
    if lastNum in numbers:
        currentNum = lasti - numbers[lastNum]
        numbers[lastNum] = lasti
        lastNum = currentNum
        lasti = i
    else:
        numbers[lastNum] = lasti
        lastNum = 0
        lasti = i
    i += 1
print(lastNum)