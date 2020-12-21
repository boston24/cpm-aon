import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout


class Graph:
    def __init__(self,listOfNodes):
        self.listOfNodes = listOfNodes

    def show(self):
        frm = []
        to = []
        for node in self.listOfNodes:
            for kid in node.kids:
                frm.append(node.name)
                to.append(kid.name)
        

        df = pd.DataFrame({ 'from':frm, 'to':to})
        G=nx.from_pandas_edgelist(df,'from','to', create_using=nx.DiGraph())
        pos = graphviz_layout(G, prog='dot')
        nx.draw(G, pos, with_labels=True, node_size=1500, alpha=1, arrows=True)
        '''nx.draw(
            G,
            node_size=2000,
            node_color='#0000FF',
            arrowsize=50,
            with_labels=True,
            #labels={n: n for n in gra.nodes},
            font_color='#FFFFFF',
            font_size=35,
            pos=nx.drawing.nx_agraph.graphviz_layout(
                G,
                prog='dot',
                args='-Grankdir=LR'
            )
        )'''
        plt.show()
    

