import sys

class Node:

    def __init__(self,name,parents,kids,time):
        self.name = name
        self.parents = parents
        self.kids = kids
        self.time = time
    
    '''def addKids(self,list):
        self.kids.extend(list)
        for kid in list:
            kid.parents.append(self)'''

    def addKids(self,list):
        #self.kids.extend(list)
        for node in list:
            if node not in self.kids:
                self.kids.append(node)
        
        try:   
            for kid in list:
                if self.isCyclic(self,kid) == False:
                    self.kids.remove(list)
                else:
                    kid.parents.append(self)
        except RecursionError:
            sys.exit("Graph not cyclic.")



    def isCyclic(self,origin,to):       
        if origin.name == to.name:
            return False
        else:
            for parent in to.parents:
                self.isCyclic(origin,parent)
