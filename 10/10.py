import collections
import math

fin = open("input.txt", "r")
data = list(map(lambda x: int(x.strip()), fin.readlines()))
data.sort()
lines = data

oneDiff = 0
twoDiff = 0
threeDiff = 0
phoneJolt = max(data) + 3
data.append(phoneJolt)
previosJolt = 0
for jolt in data:
    diff = jolt - previosJolt
    if diff == 1:
        oneDiff += 1
    elif diff == 2:
        twoDiff += 1
    elif diff == 3:
        threeDiff += 1
    previosJolt = jolt
print(oneDiff * threeDiff)

#### PART 2 IS CURRENTLY NOT WORKING. IT STILL NEEDS MORE WORK

# data.remove(phoneJolt)
# data.insert(0, 0)
# twoBranches = 0
# threeBranches = 0
# i = 0
# while i < len(data):
#     currentJolt = data[i]
#     branches = 0
#     j = i + 1
#     while j < len(data) and data[j] <= (currentJolt + 3):
#         branches += 1
#         j += 1
#     if branches == 2:
#         twoBranches += 1
#     elif branches == 3:
#         threeBranches += 1
#     if (j-1) != i:
#         i = j - 1
#     else:
#         i = j
#print(twoBranches)
#print(threeBranches)
#print((twoBranches*2) * (threeBranches*4))