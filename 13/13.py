import math
import sys

fin = open("input.txt", "r")
data = list(map(lambda x: x.strip(), fin.readlines()))

#### PART 1
# earliestTime = int(data[0])
# times = list(filter(lambda x: x != "x", data[1].split(",")))
# times = list(map(lambda x: int(x), times))

# smallestTime = sys.maxsize
# smallestID = -1
# for time in times:
#     smallestMult = math.ceil(earliestTime / time)
#     if smallestMult*time < smallestTime:
#         smallestTime = smallestMult*time
#         smallestID = time
# print((smallestTime - earliestTime) * smallestID)

times = list(map(lambda x: int(x) if x != "x" else 0, data[1].split(",")))

actualTimes = []
for time in times[1:]:
    if time != 0:
        actualTimes.append((time, times.index(time)))

startTime = 100000000000000 % times[0]
startTime = times[0] - startTime + 100000000000000
#startTime = times[0]
foundTime = False
while not foundTime:
    startTime += times[0]
    foundTime = True
    for pair in actualTimes:
        value, offset = pair
        if ((startTime + offset) % value) != 0:
            foundTime = False
            break
print(startTime)
