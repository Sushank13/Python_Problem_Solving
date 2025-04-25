class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=None
    
    def is_empty(self):
        return True if self.head is None else False
    
    def add_at_end(self,node):
        # input validation check
        if not isinstance(node, Node):
            raise TypeError("Only Node instances can be added")
        if self.is_empty():
            self.head=node
            return f"{node.data} inserted at the end"
        current_node=self.head
        while current_node.next is not None: # traverse the linked list till you find the last node
            current_node=current_node.next
        current_node.next=node # point the last node to the new node instead of None
        return f"{node.data} inserted at the end"
    
    def add_at_head(self,node):
        # input validation check
        if not isinstance(node,Node):
            raise TypeError("Only Node instances can be added")
        # point new node to the address in head and then point head to the new node
        #no need to use a temp variable as we are modifying the node itself and the head
        node.next,self.head=self.head,node
        return f"{node.data} inserted at the front"
    
    def delete_from_head(self):
        if self.is_empty():
            return None
        node_to_removed=self.head
        # point head to the address in the next pointer of first node.
        self.head=self.head.next
        # set next address of the node to be removed to None to completely unlink it
        node_to_removed.next=None
        return f"{node_to_removed.data} deleted"
        
    def delete_last_node(self):
        if self.is_empty():
            return None
        if self.head.next is None: # edge case:only one node exists
            node_to_be_removed=self.head
            self.head=None
            return f"Only Node ({node_to_be_removed.data}) Deleted" 
        #if the edge case of single node is not included then,
        #that node will never get deleted
        current_node=self.head
        prev_node=self.head
        while current_node.next is not None:
            prev_node=current_node # to get second last node
            current_node=current_node.next
        prev_node.next=None
        return f"Last Node ({current_node.data}) Deleted"
    
    def delete_node_by_value(self,value):
        if self.is_empty():
            return "Linked List is Empty"
        #edge case: if value is at the head (whether only node or not)
        if self.head.data==value:
            node_to_be_deleted=self.head
            self.head=node_to_be_deleted.next 
            node_to_be_deleted.next=None
            return f"Value {value} Deleted"
        current_node=self.head
        prev_node=self.head
        while current_node:
            if current_node.data==value:
                prev_node.next=current_node.next
                current_node.next=None
                return f"Value {current_node.data} Deleted"
            prev_node,current_node=current_node,current_node.next
        return "Value Not Found in the Linked List"
                
    def find_node(self,value):
        if self.is_empty():
            return "Linked List is empty"
        current_node=self.head
        while current_node:
            if current_node.data==value:
                return f"Node {current_node.data} found at address {current_node}"
            current_node=current_node.next
        return "Node Does not Exist" # edge case: value not present     
    
    def traverse(self):
        if self.is_empty():
            return "Linked List is Empty"
        current_node=self.head 
        while current_node:
            print(current_node.data, end="->")
            current_node=current_node.next
        print("None")   
        
node1=Node(3)
my_linked_list=LinkedList()
print(my_linked_list.add_at_end(node1))
my_linked_list.traverse()
node2=Node(10)
print(my_linked_list.add_at_end(node2))
my_linked_list.traverse()
node3=Node(20)
print(my_linked_list.add_at_head(node3))
my_linked_list.traverse()
print(my_linked_list.find_node(10))
print(my_linked_list.delete_node_by_value(3))
my_linked_list.traverse()
print(my_linked_list.delete_from_head())
my_linked_list.traverse()
print(my_linked_list.delete_last_node())
my_linked_list.traverse()
print(my_linked_list.delete_last_node())
print(my_linked_list.traverse())
        



        

        
     


            
                



            
    
    