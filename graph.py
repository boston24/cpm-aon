import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout


class Graph:
    def __init__(self,listOfNodes):
        self.listOfNodes = listOfNodes

    def show(self,path):
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
    

