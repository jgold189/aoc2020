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



###### PART 2 Brute force by me. Takes forever to run
# times = list(map(lambda x: int(x) if x != "x" else 0, data[1].split(",")))

# actualTimes = []
# for time in times[1:]:
#     if time != 0:
#         actualTimes.append((time, times.index(time)))

# startTime = 100000000000000 % times[0]
# startTime = times[0] - startTime + 100000000000000
# #startTime = times[0]
# foundTime = False
# while not foundTime:
#     startTime += times[0]
#     foundTime = True
#     for pair in actualTimes:
#         value, offset = pair
#         if ((startTime + offset) % value) != 0:
#             foundTime = False
#             break
# print(startTime)


#Too efficient not to include
#All credit to https://www.reddit.com/r/adventofcode/comments/kc4njx/2020_day_13_solutions/gfop2hb/
#Gotta love Wolfram Alpha
ids = list(data[1].split(','))
print('https://www.wolframalpha.com/input/?i=0+%3D+' + '+%3D+'.join(['((n+%2B+{})+mod+{})'.format(i, n) for i, n in enumerate(ids) if n != 'x']))