# A lot of repeated operations throughout the code that should be cleaned up, but development speed is the name of the game here
# Also a few hardcoded values in there to again speed up development time

def checkRules(indexes, rule, correctTickets):
    possibleIndexes = indexes
    for ticket in correctTickets:
        ticketNums = [int(x) for x in ticket.split(",")]
        for i in range(len(ticketNums)):
            if i in possibleIndexes:
                number = ticketNums[i]
                if not ((number >= rule[0][0] and number <= rule[0][1]) or (number >= rule[1][0] and number <= rule[1][1])):
                    possibleIndexes.remove(i)
    return possibleIndexes



fin = open("input.txt", "r")
data = [x.strip() for x in fin.readlines()]

ticketFields = data[:data.index("")]
tickets = data[data.index("")+1:]
tickets.pop(0)
tickets.pop(1)
tickets.pop(1)

allRules = []
for field in ticketFields:
    rules = field.split(": ")[1]
    rules = rules.split(" or ")
    singleRule = []
    for rule in rules:
        singleRule.append((tuple([int(x) for x in rule.split("-")])))
    allRules.append(singleRule)

#Could be made more efficient at the cost of memory using an dictionary containing all values
errors = []
correctTickets = []
for ticket in tickets:
    validTicket = True
    ticketNums = [int(x) for x in ticket.split(",")]
    for number in ticketNums:
        validNumber = False
        for rule in allRules:
            if (number >= rule[0][0] and number <= rule[0][1]) or (number >= rule[1][0] and number <= rule[1][1]):
                validNumber = True
                break
        if not validNumber:
            errors.append(number)
            validTicket = False
    if validTicket:
        correctTickets.append(ticket)
print("Part 1:", sum(errors))


ruleIndexes = [[i for i in range(20)] for _ in range(len(allRules))]
ruleIndexLengthSum = -1
while ruleIndexLengthSum != len(ruleIndexes):
    for i in range(len(allRules)):
        rule = allRules[i]
        possibleIndexes = ruleIndexes[i]
        if len(possibleIndexes) != 1:
            ruleIndexes[i] = checkRules(possibleIndexes, rule, correctTickets)
        if len(ruleIndexes[i]) == 1:
            removeValue = ruleIndexes[i][0]
            for j in range(len(ruleIndexes)):
                if i != j:
                    try:
                        ruleIndexes[j].remove(removeValue)
                    except ValueError:
                        pass
    ruleIndexLengthSum = sum([len(x) for x in ruleIndexes])

result = 1
myTicket = [int(x) for x in correctTickets[0].split(",")]
for index in ruleIndexes[:6]:
    result *= myTicket[index[0]]
print("Part 2:", result)
