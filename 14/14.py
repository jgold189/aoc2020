import copy

def decimalToBinary(n):  
    return bin(n).replace("0b", "")  

##### PART 1
# def maskBinary(mask, bin):
#     maskedBin = list(bin)
#     for i in range(len(mask)):
#         if mask[i] != "X":
#             maskedBin[i] = mask[i]
#     return "".join(maskedBin)

#### PART 2
def maskBinary(mask, bin):
    maskedList = [[]]
    maskedBin = list(bin)
    for i in range(len(mask)):
        if mask[i] == "X":
            maskedBin[i] = "X"
        elif mask[i] == "1":
            maskedBin[i] = "1"
    
    for i in range(len(maskedBin)):
        #print(maskedList)
        if mask[i] == "X":
            #This is so when we keep adding stuff to the list it doesn't go forever
            length = len(maskedList)
            for j in range(length):
                temp = copy.deepcopy(maskedList[j])
                maskedList[j].append("0")
                temp.append("1")
                maskedList.append(temp)
        else:
            for entry in maskedList:
                entry.append(maskedBin[i])
    return list(map(lambda x: "".join(x), maskedList))


fin = open("input.txt", "r")
data = list(map(lambda x: x.strip(), fin.readlines()))

#### PART 1
# memory = {}
# mask = ""
# for line in data:
#     if line[0:4] == "mask":
#         mask = line.split(" = ")[1]
#     else:
#         mem, val = line.split(" = ")
#         mem = mem[4:].strip("]")
#         val = decimalToBinary(int(val))
#         val = ("0" * (36-len(val))) + val
#         val = maskBinary(mask, val)
#         memory[mem] = int(val, 2)

##### PART 2
memory = {}
mask = ""
for line in data:
    if line[0:4] == "mask":
        mask = line.split(" = ")[1]
    else:
        mem, val = line.split(" = ")
        mem = mem[4:].strip("]")
        mem = decimalToBinary(int(mem))
        mem = ("0" * (36-len(mem))) + mem
        memList = maskBinary(mask, mem)
        for mem in memList:
            #print(int(mem, 2))
            memory[int(mem, 2)] = int(val)


print(sum([memory[key] for key in memory]))