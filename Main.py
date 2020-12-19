from node import Node
from graph import Graph
from data import *

def getCPM(graph):
    list = []
    for node in graph.listOfNodes:
        if not node.kids:
            path = []
            print("Node " + str(node.name) + " has no kids")
            list.append(getCPMlastNode(node,path))
    return list



def getCPMlastNode(node, path):
    path.append(node)
    if not node.parents:
        print(str(node.name) + " has no parent nodes")
        return node.time
    else:
        out = []
        for parent in node.parents:
            print(str(node.name) + " has parent nodes")
            out.append(node.time + getCPMlastNode(parent, path))
        return max(out)


graph = Graph(list)
'''for cpm, path in getCPM(graph):
    print(str(cpm) + ": ")
    for i in path:
        print(i.name, end=", ")'''

for i in getCPM(graph):
    print(i)