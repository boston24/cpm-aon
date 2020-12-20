from node import Node
from graph import Graph
from data import *

def getCPM(graph):
    dict = {}
    for node in graph.listOfNodes:
        if not node.kids:
            path = []
            paths = []
            #print("Node " + str(node.name) + " has no kids")
            dict.update(getCPMlastNode(node,path,paths))
    while len(dict)>1:    
        del dict[min(dict)]
    return dict



def getCPMlastNode(node, path, paths):
    if path:
        correctPath(node,path)
    else:
        path.append(node)
    
    if not node.parents:
        paths.append(path)
        return {node.time : ""}
    else:
        out = []
        for parent in node.parents:
            #print("WYpisuje: " + str(getCPMlastNode(parent, path,paths)))
            key = next(iter(getCPMlastNode(parent, path,paths)))
            out.append(node.time + key)
    

    return {max(out) : [paths[out.index(max(out))]] }


def correctPath(node, path):
    if node in path[-1].parents:
        path.append(node)
        return path
    else:
        del path[-1]
        return correctPath(node,path)

graph = Graph(list)

for key, value in getCPM(graph).items():
    print(key)
    for i in value:
        for node in i: 
            print(node.name, end=" ")
