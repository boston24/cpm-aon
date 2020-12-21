import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self,listOfNodes):
        self.listOfNodes = listOfNodes

    def show(self):
        frm = []
        to = []
        '''for node in self.listOfNodes:
            kids = []
            frm.append(node.name)
            for kid in node.kids:
                kids.append(kid)
            to.append(kids)'''
        for node in self.listOfNodes:
            for kid in node.kids:
                frm.append(node.name)
                to.append(kid.name)
        

        df = pd.DataFrame({ 'from':frm, 'to':to})
        G=nx.from_pandas_edgelist(df,'from','to', create_using=nx.DiGraph())
        nx.draw(G, with_labels=True, node_size=1500, alpha=0.3, arrows=True)
        #&nbsp;
        plt.show()
    

