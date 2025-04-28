class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

#creating nodes
node1=Node(10) 
node2=Node(5)
node3=Node(15)
node4=Node(2)
node5=Node(7)

#linking the nodes
root=node1

root.left=node2
root.right=node3

node2.left=node4
node2.right=node5

#pre-order traversal using recursion
def pre_order_traversal(node):
    if node: # if node is not None
        print(node.data,end=" ")
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)
        
#in-order using recursion
def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.data,end=" ")
        in_order_traversal(node.right)

#post-order using recursion
def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.data,end=" ")

#function calls
pre_order_traversal(root) # output: 10 5 2 7 15 (tree copying)
print()
in_order_traversal(root) # output: 2 5 7 10 15 (sorted data)
print()
post_order_traversal(root) # output: 2 7 5 15 10
