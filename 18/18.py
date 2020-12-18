#This solution is honestly hilarious and I love it.

class Overload():
    def __init__(self, val):
        self.val = val

    def __sub__(self, other):
        return Overload(self.val * other.val)

    def __add__(self, other):
        return Overload(self.val + other.val)

    def __mul__(self, other):
        return Overload(self.val + other.val)


def solve(problem):
    updatedProblem = []
    for char in problem:
        if char in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            updatedProblem.append("Overload(")
            updatedProblem.append(char)
            updatedProblem.append(")")
        elif char == "*":
            updatedProblem.append("-")
        elif char == "+":
            updatedProblem.append("*")
        else:
            updatedProblem.append(char)
    updatedProblem = "".join(updatedProblem)
    answer = eval(updatedProblem)
    return answer.val


fin = open("input.txt", "r")
data = [x.strip() for x in fin.readlines()]

answers = []
for problem in data:
    answers.append(solve(problem))
print(sum(answers))
