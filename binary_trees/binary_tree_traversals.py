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

#DFS:pre-order traversal using recursion
def pre_order_traversal(node):
    if node: # if node is not None
        print(node.data,end=" ")
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)
        
#DFS:in-order using recursion
def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.data,end=" ")
        in_order_traversal(node.right)

#DFS:post-order using recursion
def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.data,end=" ")
        
# breadth first search traversal
from collections import deque
def bfs(root):
    if not root: # tree is empty
        return None
    q=deque()
    q.append(root)
    while q:
        current=q.popleft()
        print(current.data,end=" ")
        if current.left is not None:
            q.append(current.left)
        if current.right is not None:
            q.append(current.right)
            
def bfs_levels_newline(root):
    if not root:
        return None
    q=deque()
    q.append(root)
    while q:
        level_size=len(q)
        for _ in range(level_size):
            current=q.popleft()
            print(current.data,end=" ")
            if current.left is not None:
                q.append(current.left)
            if current.right is not None:
                q.append(current.right)
        print()
                   
#function calls
pre_order_traversal(root) # output: 10 5 2 7 15 (tree copying)
print()
in_order_traversal(root) # output: 2 5 7 10 15 (sorted data)
print()
post_order_traversal(root) # output: 2 7 5 15 10
print()
bfs(root)
print()
bfs_levels_newline(root)