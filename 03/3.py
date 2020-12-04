from functools import reduce

def CheckSlope(data, right, down):
    TREE = "#"
    y = len(data)
    x = len(data[0])
    xpos = 0
    treeCounter = 0
    for i in range(down, y, down):
        xpos += right
        xpos %= x
        if data[i][xpos] == TREE:
            treeCounter += 1
    return treeCounter


if __name__ == "__main__":
    fin = open("input.txt", "r")
    data = list(map(lambda x: x.strip(), fin.readlines()))

    slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
    results = []
    for slope in slopes:
        results.append(CheckSlope(data, slope[0], slope[1]))

    multResults = reduce(lambda x,y: x*y, results)
    print(multResults)