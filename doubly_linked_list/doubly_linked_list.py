"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next
    
    def get_prev(self):
        return self.prev

    def set_next(self, new_next=None):
        self.next = new_next
    
    def set_prev(self, new_prev=None):
        self.prev = new_prev
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value, prev=None, next=self.head)
        
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        
        else:
            self.head.set_prev(new_node)
            self.head = new_node

        self.length += 1
        


        
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None and self.tail is None:
            return None

        value = self.head.get_value()
        
        if self.head is self.tail:
            self.head = None
            self.tail = None
        
        else:
            self.head = self.head.get_next()
            self.head.set_prev()
        
        self.length -= 1
        return value
            
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value, prev=self.tail)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
        
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail is None and self.head is None:
            return None

        value = self.tail.get_value()

        if self.tail is self.head:
            self.tail = None
            self.head = None
        
        else:
            self.tail = self.tail.get_prev()
            self.tail.set_next()

        self.length -= 1
        return value
        
                    
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.get_value())
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.get_value())

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.tail is None and self.head is None:
            return None

        elif self.tail is self.head:
            self.head = None
            self.tail = None
            self.length -= 1

        elif node is self.head:
            self.remove_from_head()
        
        elif node is self.tail:
            self.remove_from_tail()

        else:
            curr_node = self.head
            prev_node = None
            next_node = self.head.get_next()

            while curr_node is not node:
                prev_node = curr_node
                curr_node = next_node
                next_node = curr_node.get_next()
            
            prev_node.set_next(next_node)
            next_node.set_prev(prev_node)
            curr_node = None
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        curr_max = self.head.get_value()
        curr_node = self.head

        while curr_node is not None:
            if curr_node.get_value() > curr_max:
                curr_max = curr_node.get_value()
            
            curr_node = curr_node.get_next()
        
        return curr_max