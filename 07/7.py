import networkx as nx
import re

def bagTotal(start):
    bagNums = 0
    for item in DG.adj[start]:
        weight = DG.edges[start, item]["weight"]
        bagNums += weight * bagTotal(item) + weight
    return bagNums

def lineParser(line):
    bag, contains = line.split("contain")
    bag = bag[0:bag.find(" bag")]

    if contains == " no other bags.":
        contains = []
    else:
        contains = contains.split(",")
        contains = list(map(lambda x: x[0:x.find("bag")].strip().split(" ", 1), contains))
    return((bag, contains))


fin = open("input.txt", "r")
rules = list(map(lambda x: lineParser(x.strip()), fin.readlines()))

DG = nx.DiGraph()
for rule in rules:
    bag, contains = rule
    DG.add_node(bag)
    for result in contains:
        DG.add_node(result[1])
        DG.add_weighted_edges_from([(bag, result[1], int(result[0]))])

#Because there is a path from shiny gold to shiny gold
shinyGoldAncestors = -1
nodes = list(DG.nodes)
for node in nodes:
    hasPath = nx.has_path(DG, node, "shiny gold")
    if hasPath:
        shinyGoldAncestors += 1
print(shinyGoldAncestors)

print(bagTotal('shiny gold'))