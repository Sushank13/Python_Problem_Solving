#define a tree node
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

# create tree nodes (write now they are not linked)
root=Node(13)
node7=Node(7)
node3=Node(3)
node8=Node(8)
node15=Node(15)
node14=Node(14)
node19=Node(19)
node18=Node(18)

#link the nodes to create a BST
root.left=node7
root.right=node15

node7.left=node3
node7.right=node8

node15.left=node14
node15.right=node19

node19.left=node18

#traverse the BST
def in_order_traversal(node):
    if node: # if tree is not empty
        in_order_traversal(node.left)
        print(node.data,end=" ")
        in_order_traversal(node.right)

in_order_traversal(root) # sorted data
        
