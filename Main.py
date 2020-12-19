from node import Node
from graph import Graph

def getCPM(graph):
    list = []
    for node in graph.listOfNodes:
        if not node.kids:
            path = []
            list.append(getCPMlastNode(node,path)-node.time)
    return list



def getCPMlastNode(node, path):
    path.append(node)
    if not node.parents:
        print(str(node.name) + " has no parent nodes")
        return node.time
    else:
        out = {}
        for parent in node.parents:
            print(str(node.name) + " has parent nodes")
            return node.time + getCPMlastNode(parent, path)


    
        



list = []
z1 = Node("z1",[],[],3)
z2 = Node("z2",[],[],8)
z3 = Node("z3",[],[],2)
z4 = Node("z4",[],[],2)
z5 = Node("z5",[],[],4)
z6 = Node("z6",[],[],6)
z7 = Node("z7",[],[],9)
z8 = Node("z8",[],[],2)
z9 = Node("z9",[],[],1)
z10 = Node("z10",[],[],2)
z11 = Node("z11",[],[],1)
z12 = Node("z12",[],[],2)
z13 = Node("z13",[],[],6)
z14 = Node("z14",[],[],5)
z15 = Node("z15",[],[],9)
z16 = Node("z16",[],[],6)
z17 = Node("z17",[],[],2)
z18 = Node("z18",[],[],5)
z19 = Node("z19",[],[],3)

list.append(z1)
list.append(z2)
list.append(z3)
list.append(z4)
list.append(z5)
list.append(z6)
list.append(z7)
list.append(z8)
list.append(z9)
list.append(z10)
list.append(z11)
list.append(z12)
list.append(z13)
list.append(z14)
list.append(z15)
list.append(z16)
list.append(z17)
list.append(z18)
list.append(z19)

z1.addKids([z4,z5])
for p in z5.parents:
    print(p.name)


graph = Graph(list)
'''for cpm, path in getCPM(graph):
    print(str(cpm) + ": ")
    for i in path:
        print(i.name, end=", ")'''

#for i in getCPM(graph):
#    print(i)