def transformLoop(val, subject, loop):
    val = 1
    for _ in range(loop):
        val *= subject
        val = val % 20201227
    return val

def transform(val, subject):
    return (val * subject) % 20201227

fin = open("input.txt", "r")
data = [int(x.strip()) for x in fin.readlines()]

dataSet = set(data)
subject = 7
loops = {}
val = 1
i = 0
bothFound = False
while not bothFound:
    i += 1
    val = transform(val, subject)
    if val in dataSet:
        loops[val] = i
        if len(loops) == len(data):
            bothFound = True

print(transformLoop(1, data[0], loops[data[1]]))
