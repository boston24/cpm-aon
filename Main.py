import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from node import Node
from graph import Graph
from data import *
from networkx.drawing.nx_agraph import graphviz_layout

def getCPM(graph):
    dict = {}
    for node in graph.listOfNodes:
        if not node.kids:
            path = []
            paths = []
            dict.update(getCPMNode(node,path,paths))
    while len(dict)>1:    
        del dict[min(dict)]
    return dict



def getCPMNode(node, path, paths):
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
            key = next(iter(getCPMNode(parent, path,paths)))
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
dict = getCPM(graph)
#dict = getCPMNode(z10,[],[])


for key, value in dict.items():
    print(key)
    for i in value:
        for node in i: 
            print(node.name, end=" ")

graph.show()            
