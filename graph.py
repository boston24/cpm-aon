import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import plotly.express as px
from networkx.drawing.nx_agraph import graphviz_layout


class Graph:
    def __init__(self,listOfNodes):
        self.listOfNodes = listOfNodes

    def showGraph(self,path):
        frm = []
        to = []
        for node in self.listOfNodes:
            for kid in node.kids:
                frm.append(node.name)
                to.append(kid.name)
        

        df = pd.DataFrame({ 'from':frm, 'to':to})
        G=nx.from_pandas_edgelist(df,'from','to', create_using=nx.DiGraph())
        pos = graphviz_layout(G, prog='dot')
        #nx.draw(G, pos, with_labels=True, node_size=1500, alpha=1, arrows=True)
        color_map=[]
        for node in G:
            if node in path:
                color_map.append('red')
            else:
                color_map.append('white')

        nx.draw(
            G,
            node_size=1500,
            node_color=color_map,
            edgecolors='black',
            arrowsize=10,
            with_labels=True,
            labels={n: n for n in G.nodes},
            font_color='black',
            font_size=15,
            pos=nx.drawing.nx_agraph.graphviz_layout(
                G,
                prog='dot',
                args='-Grankdir=LR'
            )
        )
        plt.show()
    
    def showTimeline(self,jobs):

        #print(jobs)

        fig,gnt = plt.subplots() 

        maxX = max([x['Finish'] for x in jobs])
        maxRow = max([x['Row'] for x in jobs])

        gnt.set_ylim(0, maxRow) 
        
        gnt.set_xlim(0, maxX) 
         
        gnt.set_yticks(range(0,maxRow)) 
        gnt.set_xticks(range(0,maxX+1))

        gnt.grid(False) 
         
        for node in jobs:
            gnt.broken_barh([(node["Start"],node["Time"])], (node["Row"]-1,1), facecolors ='tab:blue',edgecolors='black')
            gnt.text(x=node["Start"]+node["Time"]/2, y=node["Row"]-0.5,s=node["Name"],ha='center',va='center',color='black')
        
        plt.show()
        #plt.savefig("gantt1.png") 

            