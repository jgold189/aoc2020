fin = open("input.txt", "r")

data = fin.readlines()

data = list(map(lambda x: int(x.strip()), data))

values = {}
for line in data:
    values[line] = line

##PART 1
for line in data:
    if (2020 - line) in values:
        print(line * (2020-line))
        #Should have an early exit when it happens here but whatever


##PART 2
smallData = list(filter(lambda x: x <= 1500, data))
for i in range(len(smallData)):
    value = 2020 - smallData[i]
    for j in range(i+1, len(smallData), 1):
        if (value - smallData[j]) in smallData:
            print(smallData[i]*smallData[j]*(value-smallData[j]))
