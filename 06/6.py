from functools import reduce

def intersection(l1, l2):
    return set(l1).intersection(l2)

fin = open("input.txt", "r")

data = list(map(lambda x: x.strip(), fin.readlines()))

#### PART 1
answerList = []
answerSet = set()
for line in data:
    if line == "":
        answerList.append(answerSet)
        answerSet = set()
    else:
        for char in line:
            answerSet.add(char)
answerList.append(answerSet)

yesSum = sum(map(lambda x: len(x), answerList))
print(yesSum)

#### PART 2
answerList = []
groupAnswers = []
for line in data:
    if line == "":
        answerList.append(reduce(intersection, groupAnswers))
        groupAnswers = []
    else:
        answers = []
        for char in line:
            answers.append(char)
        groupAnswers.append(answers)
answerList.append(reduce(intersection, groupAnswers))

yesSum = sum(map(lambda x: len(x), answerList))
print(yesSum)