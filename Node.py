class Node:

    def __init__(self,name,parents,kids,time):
        self.name = name
        self.parents = parents
        self.kids = kids
        self.time = time
    
    def addKids(self,list):
        self.kids.extend(list)
        for kid in list:
            kid.parents.append(self)

