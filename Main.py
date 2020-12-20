from node import Node
from graph import Graph
from data import *

def getCPM(graph):
    list = []
    for node in graph.listOfNodes:
        if not node.kids:
            path = []
            paths = []
            #print("Node " + str(node.name) + " has no kids")
            list.append(getCPMlastNode(node,path,paths))
    return list



def getCPMlastNode(node, path, paths):
    if path:
        correctPath(node,path)
        #print("\nPath: ")
        #for i in path:
        #    print(i.name, end = ", ")
    else:
        path.append(node)
    
    if not node.parents:
        #print(str(node.name) + " has no parent nodes")
        paths.append(path)
        return node.time
    else:
        out = []
        for parent in node.parents:
            #print(str(node.name) + " has parent nodes")
            out.append(node.time + getCPMlastNode(parent, path,paths))
        
    print("\nFinal path: ")
    for i in paths[out.index(max(out))]:
        print(i.name, end=", ")
    print("\n")    
    return max(out)


def correctPath(node, path):
    if node in path[-1].parents:
        path.append(node)
        return path
    else:
        del path[-1]
        return correctPath(node,path)

graph = Graph(list)

for i in getCPM(graph):
    print(i)

