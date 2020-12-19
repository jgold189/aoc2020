#Okay so this is now a mess but let me explain
#The problem presented rules to a language and asked you to find what strings were valid for the language or not
#There were no loops in the original langauges rules for part 1 so I said "Great, I'll convert these rules to a regular expression since that is valid"
#And it worked great and was pretty clean and very fast for part 1.
#Then part two hit
#The rules were changed so two rules now had loops
#The rules were:
# 8: 42 | 42 8
# 11: 42 31 | 42 11 31
#While slightly hardcoded rule 8 was simple, it was just (42)+
#AKA one or more matches of rule 42
#Rule 11 on the other hand is not possible in standard regular expressions
#It would be equivalent to 42^n 31^n where n>=1
#AKA a classic context free language
#These balanced expressions are not possible in standard regex. And as far as I can tell they are not possible without recursive regex
#Python re does not support recursive regex and thus as far as I know can not match this language.
#As such I crudely hardcoded in rule 11 to basically repeat the pattern 6 times and I guessed the problem would not have more than 6 possible repetitions

import re
from functools import lru_cache

@lru_cache(maxsize=None)
def buildRegex(ruleNum):
    result = []
    if rules[ruleNum] == "a" or rules[ruleNum] == "b":
        result.append(rules[ruleNum])
    elif ruleNum == 8:
        result.append("(")
        result.extend(buildRegex(42))
        result.append(")+")
    #Scary mess
    elif ruleNum == 11:
        result.append("((")
        result.extend(buildRegex(42))
        result.extend(buildRegex(31))
        result.append(")")
        for i in range(2,7):
            result.append("|(")
            for _ in range(i):
                result.extend(buildRegex(42))
            for _ in range(i):
                result.extend(buildRegex(31))
            result.append(")")
        result.append(")")
    elif any(isinstance(i, list) for i in rules[ruleNum]):
        result.append("((")
        for subRules in rules[ruleNum][0]:
            result.extend(buildRegex(subRules))
        result.append(")|")

        result.append("(")
        for subRules in rules[ruleNum][1]:
            result.extend(buildRegex(subRules))
        result.append("))")
    else:
        #If normal rules
        result.append("(")
        for subRules in rules[ruleNum]:
            result.extend(buildRegex(subRules))
        result.append(")")
    return result

fin = open("input.txt", "r")
data = [x.strip() for x in fin.readlines()]
messages = data[data.index("")+1:]
dataRules = data[:data.index("")]

rules = {}
for rule in dataRules:
    num, subRules = rule.split(":")
    if "a" in subRules:
        rules[int(num)] = "a"
    elif "b" in subRules:
        rules[int(num)] = "b"
    elif "|" in subRules:
        subRules = list(map(lambda x: [int(y) for y in x.strip().split(" ")], subRules.split("|")))
        rules[int(num)] = subRules
    else:
        rules[int(num)] = [int(x) for x in subRules.strip().split(" ")]


regexBuild = buildRegex(0)
regexBuild.append("$")
regexBuild.insert(0, "^")
regex = "".join(regexBuild)

matchedMessages = 0
for message in messages:
    if re.match(regex, message):
        matchedMessages += 1
print(matchedMessages)
