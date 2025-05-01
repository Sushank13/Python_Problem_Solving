#refer Python Notes for reference image of BST
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None # initialize root pointer as None
    
    def add(self,node):
        if not isinstance(node,Node):
            raise TypeError("Only object of Type Node Accepted")
        if self.root is None: # tree is empty
            self.root=node
            return "Node added as root (Tree was empty)"
        current=self.root
        while current:
            if node.data<current.data:
                if current.left is None:
                    current.left=node
                    return "Node Inserted in left sub-tree"
                current=current.left # move forward the current pointer to the address in current node's left pointer 
            elif node.data>current.data:
                if current.right is None:
                    current.right=node
                    return "Node inserted in right sub-tree"
                current=current.right # move forward the current pointer to the addres in current node's right pointer
            else: #duplicate value
                return "No Duplicates Allowed"
            
    def find(self,value):
        if self.root is None: # tree is empty
            return "Tree is Empty"
        current=self.root
        while current:
            if value<current.data:
                current=current.left
            elif value>current.data:
                current=current.right
            else: #value matches
                return f"Value {current.data} found at address {current}"
        return "Value Does not Exist in the BST"
    
    def delete(self,value):
        current=self.root
        prev=None # to keep track of the previous node (parent)
        while current:
            if value<current.data: #move to left sub-tree
                prev,current=current,current.left
            elif value>current.data: #move to right sub-tree
                prev,current=current,current.right
            else: #match found
                print(f"Left:{current.left}, data: {current.data}, Right: {current.right}")
                # Case 1: node to be deleted is a leaf node (has no children)
                if current.left is None and current.right is None: 
                    if prev is None: #edge case: root node to be deleted and is the only node
                        self.root=None
                        return f"Root Node {value}Deleted (Had No Children)"
                    elif prev.left == current: # check if the current node is left child of the parent
                        prev.left=None
                        return f"Left Leaf Node {value} Deleted"
                    else:#current node is right child of the parent
                        prev.right=None
                        return f"Right Leaf Node {value} Deleted" 
                # Case2: node to be deleted has 1 child (right child)
                elif current.left is None: 
                    if prev is None: # edge case: root node to be deleted and has right child
                        self.root=current.right
                        return f"Root Node {value} deleted (Had a Right Child)"
                    elif prev.left == current: # check if the current node is left child of the parent
                        prev.left=current.right
                        return f"Value {value} Deleted. It had 1 Right Child"
                    else: #current node is right child of the parent
                        prev.right=current.right
                        return f"Value {value} Deleted. It had 1 Right Child"
                # Case2: node to be deleted has 1 child (left child)
                elif current.right is None: 
                    if prev is None: # edge case: root node to be deleted and has left child
                        self.root=current.left
                        return f"Root Node {value} deleted (Had a Left Child)"
                    elif prev.left == current:
                        prev.left=current.left
                        return f"Value {value} Deleted. It had 1 Left Child"
                    else: 
                        prev.right=current.left
                        return f"Value {value} Deleted. It had 1 Left Child"
                # Case3: Node to be deleted has both children
                else: 
                    successor_parent,successor=self.get_in_order_successor(current) # find in-order successor
                    current.data=successor.data # replace value of node to be deleted with in-order successor
                    # delete the successor
                    if successor_parent.left==successor: # successot was left child
                        successor_parent.left=successor.right # successor can never have a left child as it is the leftmost itself
                    else: # successor was the right child
                        successor_parent.right=successor.right   
                return f"Node {value} Deleted. It had both Children"               
        return f"Value {value} Does Not Exist in the BST"
    
    def get_in_order_successor(self,node):
        parent=node # need parent of the successor as its child pointer(the successor's address) will be re-assignd 
        successor=node.right
        while successor.left:
            parent=successor
            successor=successor.left
        return parent,successor
            
    def in_order_traversal(self,node):
        if node:
            self.in_order_traversal(node.left)
            print(node.data,end=" ")
            self.in_order_traversal(node.right)

#node13=13
my_bst=BST()
#my_bst.add_node(node13) # return Type Error      
node13=Node(13)
print(my_bst.add(node13)) 
my_bst.in_order_traversal(my_bst.root)
print()
print(my_bst.add(node13)) # check for duplicate value
node7=Node(7)
print(my_bst.add(node7))
my_bst.in_order_traversal(my_bst.root)
print()
node15=Node(15)
print(my_bst.add(node15))
my_bst.in_order_traversal(my_bst.root)
print()
node14=Node(14)
print(my_bst.add(node14))
my_bst.in_order_traversal(my_bst.root)
print()
node3=Node(3)
print(my_bst.add(node3))
my_bst.in_order_traversal(my_bst.root)
print()
node8=Node(8)
print(my_bst.add(node8))
my_bst.in_order_traversal(my_bst.root)
print()
# changing the insertion order 
# add node 18 first, before 19
node18=Node(18)
print(my_bst.add(node18))
my_bst.in_order_traversal(my_bst.root)
print()
node19=Node(19)
print(my_bst.add(node19))
my_bst.in_order_traversal(my_bst.root)
print()
# this changes the shape of the BST (19 will be on right of 18)
# but still the tree is "reasonably balanced" and hence, we get sorted
#data for in-order traversal
print(my_bst.find(2))
print(my_bst.find(8))
print(my_bst.delete(2)) #value to be deleted does not exist
print(my_bst.delete(3)) # delete a left leaf node
my_bst.in_order_traversal(my_bst.root)
print()
print(my_bst.delete(7)) # delete a node that has a right child
my_bst.in_order_traversal(my_bst.root)
print()
print(my_bst.delete(13)) # delete a node that has both children
my_bst.in_order_traversal(my_bst.root)
print()
print(my_bst.delete(15)) # delete a node that has a right child
my_bst.in_order_traversal(my_bst.root)
print()
print(my_bst.delete(19)) # delete a right leaf node
my_bst.in_order_traversal(my_bst.root)
print()
print(my_bst.delete(14)) # delete a node that has both children
my_bst.in_order_traversal(my_bst.root)
print()
print(my_bst.delete(18)) # delete root when it has 1 child
my_bst.in_order_traversal(my_bst.root)
print()
print(my_bst.delete(8)) # delete last value
my_bst.in_order_traversal(my_bst.root)
print()