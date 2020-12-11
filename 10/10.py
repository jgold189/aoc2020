from functools import lru_cache
import math

@lru_cache(maxsize=None)
def adapterPath(adapter):
    if adapter in data:
        if adapter == data[0]:
            return 1
        elif adapter < 0:
            return 0
        else:
            return adapterPath(adapter-1) + adapterPath(adapter-2) + adapterPath(adapter-3)
    else:
        return 0

fin = open("input.txt", "r")
data = list(map(lambda x: int(x.strip()), fin.readlines()))
data.sort()
lines = data

#### PART 1
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

#### PART 2
data.insert(0, 0)
print(adapterPath(data[-1]))