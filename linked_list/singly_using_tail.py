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
    
    def del_from_front(self):
        if self.head is None:
            return "List is empty. Nothing to delete"
        current=self.head
        self.head,current.next=current.next,None
        return f"{current.data} node deleted from front"
    
    def pop(self):
        if self.head is None:
            return "List is empty. Nothing to delete"
        if self.head==self.tail: # only one element
            self.head=None
            self.tail=None
            return f"Last Node Deleted (There was Only One Element)"
        current=self.head
        prev=None
        while current:
            if current==self.tail:
                prev.next,self.tail=None,prev
            prev,current=current,current.next
            return f"Last node {current.data} deleted"
        
    def delete(self,value):
        if self.head is None:
            return "List is empty. Nothing to delete"
        if self.head == self.tail: # only one element
            if self.head.data==value:
                self.head=None
                self.tail=None
                return f"Node {value} deleted"
            else:
                return f"Node {value} does not exist"
        current=self.head
        prev=None
        while current:
            if current.data==value:
                prev.next,current.next=current.next,None
                return f"Node {value} Deleted"
            prev,current=current,current.next
    
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
    
    def reverse(self):
        if self.is_empty():
            return f"List is Empty"
        #initialize three pointers
        prev=None
        current=self.head
        next_address=None # to keep track of address in current node's next as it will be modified
        while current:
            next_address=current.next # track address of next node
            current.next=prev # reverse links by changing the address in the current node to the address held in prev pointer
            #move pointers forward
            prev=current
            current=next_address
        self.head=prev
        return "Linked List Reversed"
    
    def has_cycle_using_set(self): # using a set()
        visited_nodes=set()
        current_node=self.head
        while current_node:
            if current_node in visited_nodes:
                return True
            visited_nodes.add(current_node)
            current_node=current_node.next
        return False 
    
    def has_cycle_using_floyd(self):
        if self.is_empty(): #list is empty, no cycle
            return False 
        slow=self.head
        fast=self.head
        while True:
            if fast is None or fast.next is None: # fast pointer reache the end, so no cycle
                return False
            slow=slow.next
            fast=fast.next.next
            if slow == fast: # cycle exists
                return True
    
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
#my_linked_list.traverse_in_reverse()
print(my_linked_list.reverse())
my_linked_list.traverse()
print(my_linked_list.has_cycle_using_set())
print(my_linked_list.has_cycle_using_floyd())
