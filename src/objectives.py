class LinkedListNode: 
    def __init__(self, value):
        self.value = value
        self.next = None # Another node




linked_list =  LinkedListNode(3)

def add_to_head(head, value):
    # creat teh new node 
    new_node = LinkedListNode (value)
    #@link up the nodes 
    new_node.next = head 

    return new_node #the start of the linked list 



    def add_to_head(tail, value):
        # creat teh new node 
    new_node = LinkedListNode (value)
    # Link the new node , to the tail 
    tail.next = new_node

    return new_node #the end of the linked list 

def add_to_head(current_node, value):
    # creat teh new node 
    new_node = LinkedListNode (value)
    next_node = Current_node.next
    # Current node p;oints to the new 
    current_node.next = new_node
    new_node.next = next_node

    return new_node #the start of the linked list 

def print_list(start_node):
    if start_node is None:
        return

    print(start_node.value)
    print(start_node.next)


  
linked_list = LinkedListNode(3)
linked_list = add_to_head(linked_list, 2)



print(linked_list.value)
print(linked_list.next.value)