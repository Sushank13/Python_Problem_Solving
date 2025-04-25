class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def add_at_end(self,node):
        if not isinstance(node,Node):
            raise TypeError("Only values of Type Node can be added")
        if self.is_empty(): #edge case: need to update both head and tail
            self.head=node
            self.tail=node
            return f"Node {node.data} added at the end (list was empty)"
        # else need to update the tail only giving us O(1) time complexity
        self.tail.next,self.tail=node,node
        return f"Node {node.data} added at the end"
    
    def add_at_front(self,node):
        if not isinstance(node,Node):
            raise TypeError("Only values of Type Node can be added")
        if self.is_empty(): #edge case: need to update both head and tail
            self.head=node
            self.tail=node
            return f"Node {node.data} is added at front (list was empty)"
        # else need to update the head only giving us O(1) time complexity
        node.next,self.head=self.head,node
        return f"Node {node.data} is added at front"
    
    def traverse(self):
        current_node=self.head
        while current_node:
            print(current_node.data, end="->")
            current_node=current_node.next
        print("None")
        
    def traverse_in_reverse(self):
        current_node=self.head
        stack=[]
        while current_node:
            stack.append(current_node.data)
            current_node=current_node.next
        while stack:
            print(stack.pop(),end="->")
        print(None)
    
    def is_empty(self):
        return True if self.head is None else False
    
my_linked_list=LinkedList()
node1=Node(12)
#print(my_linked_list.add_at_end(node1))
print(my_linked_list.add_at_front(node1))
my_linked_list.traverse()
node2=Node(30)
print(my_linked_list.add_at_front(node2))
my_linked_list.traverse()
node3=Node(27)
print(my_linked_list.add_at_end(node3))
print(f"Tail:{my_linked_list.tail.data}")
print(f"Head:{my_linked_list.head.data}")
my_linked_list.traverse()
my_linked_list.traverse_in_reverse()