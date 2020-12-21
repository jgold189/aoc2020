from functools import reduce

def intersection(list1, list2):
    temp = set(list2) 
    list3 = [value for value in list1 if value in temp] 
    return list3

fin = open("input.txt", "r")
data = [x.strip(")\n") for x in fin.readlines()]

foods = []
aller = {}
for line in data:
    ingredients, allergens = line.split(" (contains ")
    ingredients = ingredients.split(" ")
    allergens = allergens.split(", ")
    foods.append((ingredients,allergens))
    for allergen in allergens:
        if allergen not in aller:
            aller[allergen] = []
        aller[allergen].append(ingredients)

fullAllergyList = []
for key in aller:
    aller[key] = reduce(intersection, aller[key])
    fullAllergyList.extend(aller[key])

#### PART 1
count = 0
for food in foods:
    for ingredient in food[0]:
        if ingredient not in fullAllergyList:
            count += 1
print(count)

#### PART 2
actualAllergens = []
toRemove = []
while len(aller):
    for key in aller:
        if len(aller[key]) == 1:
            actualAllergens.append((aller[key][0], key))
            for subKey in aller:
                if subKey != key:
                    try:
                        aller[subKey].remove(aller[key][0])
                    except ValueError as e:
                        pass
            toRemove.append(key)
    for key in toRemove:
        aller.pop(key)
    toRemove = []

actualAllergens.sort(key=lambda x: x[1])
actualAllergens = [x[0] for x in actualAllergens]
print(",".join(actualAllergens))