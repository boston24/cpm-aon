import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from node import Node
from graph import Graph
from data import *
from networkx.drawing.nx_agraph import graphviz_layout
import plotly.express as px

def getCPM(graph):
    dict = {}
    for node in graph.listOfNodes:
        if not node.kids:
            path = []
            paths = []
            dict.update(getCPMNode(node,path,paths))
    #print("\nMax key: "+str(max(dict, key=int)))
    max_key = max(dict, key=int)
    #while len(dict)>1:    
    #    del dict[min(dict)]
    #return dict
    return {max_key:dict[max_key]}



def getCPMNode(node, path, paths):
    if path:
        correctPath(node,path)
        #print("\nCurrent path:", end=" ")
        #for i in path:
        #    print(i.name, end=" ")
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

def getCPMNodeMinPath(node, path, paths):
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
    

    return {min(out) : [paths[out.index(min(out))]] }


def correctPath(node, path):
    if node in path[-1].parents:
        path.append(node)
        return path
    else:
        del path[-1]
        return correctPath(node,path)

def makeListForTimetable(list):
    jobs = []
    rows = []
    for i in range(len(list)):
        free_space = []
        if i==0:
            free_space.append(1)
        node = list[i]
        time = node.time
        name=node.name
        for key,value in getCPMNode(node,[],[]).items():
            finish=key
            start=key-node.time
            if not i==0:  
                for j in range(i):
                    node_temp = list[j]
                    for key,value in getCPMNode(node_temp,[],[]).items():
                        finish_temp = key
                    if(start>=finish_temp):
                        free_space.append(rows[j])
                    else:
                        if rows[j] in free_space:
                            free_space = [i for i in free_space if i != rows[j]]
            if not free_space:
                free_space.append(max(rows)+1)
                rows.append(free_space[0])
            else:
                rows.append(free_space[0])

        jobs.append(dict(Name=name, Start=start, Finish=finish, Row=free_space[0], Time=time))
    
    return jobs


#graph = Graph(list)

''' MAX PATH TO NODE '''
'''
node_temp = z19
print(node_temp.time)
cpm_temp = getCPMNode(node_temp,[],[])
for key, value in cpm_temp.items():
    print(key)
    for i in value:
        for node in i:
            print(node.name, end=" ")
'''

''' CPM - MAX PATH '''
cpm = getCPM(graph)
path=[]

for key, value in cpm.items():
    print("\nCPM: "+str(key))
    for i in value:
        for node in i: 
            print(node.name, end=" ")
            path.append(node.name)


''' MIN PATH '''
'''
node_min = z19
print("Shortest path to "+str(node_min.name))
latest = getCPMNodeMinPath(node_min,[],[])
for key, value in latest.items():
    print(key - node_min.time)
    for i in value:
        for node in i:
            print(node.name, end=" ") 
'''

graph.showGraph(path)      
graph.showTimeline(makeListForTimetable(list))      
