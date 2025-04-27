class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
# create nodes. Right now,these are not connected        
root=Node("R")
nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')
nodeE = Node('E')
nodeF = Node('F')
nodeG = Node('G')

#link the nodes to create the binary tree
root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

#test
print(root.left.right.left)
print(root.right.right.left.data)