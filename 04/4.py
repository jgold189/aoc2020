import re

##### DATA LOAD
fin = open("input.txt", "r")
messyData = fin.readlines()

data = []
passport = {}
for line in messyData:
    if line == "\n":
        data.append(passport)
        passport = {}
    else:
        fields = line.strip().split(" ")
        for field in fields:
            key, value = field.split(":")
            passport[key] = value
data.append(passport)

##### PART 1
validP1Passports = 0
requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
for pport in data:
    isValid = True
    for rfield in requiredFields:
        if rfield not in pport:
            isValid = False

    if isValid:
        validP1Passports += 1

print(validP1Passports)

##### PART 2
validP2Passports = 0
eyeColor = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
for pport in data:
    validFields = 0
    if "byr" in pport:
        byr = int(pport["byr"])
        if len(str(byr)) == 4 and byr >= 1920 and byr <= 2002:
            validFields += 1
    
    if "iyr" in pport:
        iyr = int(pport["iyr"])
        if len(str(iyr)) == 4 and iyr >= 2010 and iyr <= 2020:
            validFields += 1

    if "eyr" in pport:
        eyr = int(pport["eyr"])
        if len(str(eyr)) == 4 and eyr >= 2020 and eyr <= 2030:
            validFields += 1

    if "hgt" in pport:
        hgt = pport["hgt"]
        if "in" in hgt:
            num = int(hgt[0:hgt.find("i")])
            if num >= 59 and num <= 76:
                validFields += 1
        elif "cm" in hgt:
            num = int(hgt[0:hgt.find("c")])
            if num >= 150 and num <= 193:
                validFields += 1

    if "hcl" in pport:
        hcl = pport["hcl"]
        regex = r"^#[0-9a-f]{6}"
        if re.match(regex, hcl):
            validFields += 1

    if "ecl" in pport:
        ecl = pport["ecl"]
        if ecl in eyeColor:
            validFields += 1
        
    if "pid" in pport:
        pid = pport["pid"]
        if len(pid) == 9:
            validFields += 1

    if validFields == 7:
        validP2Passports += 1

print(validP2Passports)
