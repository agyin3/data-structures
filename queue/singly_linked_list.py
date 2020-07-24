class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node
    def get_value(self):
        return self.value
    def get_next(self):
        return self.next_node
    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node

        if self.length == 0:
            self.tail = new_node
        
        self.length += 1

    def add_to_tail(self, value):
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        
        self.tail = new_node
        self.length += 1

    def remove_head(self):
        if self.tail is None and self.head is None:
            return None

        curr_value = self.head.get_value()
        if self.head is self.tail:
            self.head = None
            self.tail = None

        else:
            self.head = self.head.get_next()
        
        self.length -= 1
        return curr_value
        
    
    def remove_tail(self):
        if self.tail is None and self.head is None:
            return None

        elif self.tail is self.head:
            curr_value = self.tail.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return curr_value

        else:
            curr_node = self.head
            old_tail = self.tail.get_value()
            
            while curr_node.get_next() is not self.tail:
                curr_node = curr_node.get_next()
            
            self.tail = curr_node
            self.tail.set_next(new_next=None)
            self.length -= 1
            return old_tail

    def contains(self, value):
        if self.tail is None and self.head is None:
            return False
        
        curr_node = self.head

        while curr_node.get_value() is not value:
            curr_node = curr_node.get_next()
            if curr_node is None:
                return False
        
        return curr_node

    def get_max(self):
        if self.head is None and self.tail is None:
            return None

        curr_node = self.head
        curr_max = self.head.get_value()

        while curr_node is not None:
            
            if curr_max <= curr_node.get_value():
                curr_max = curr_node.get_value()
            curr_node = curr_node.get_next()
        
        return curr_max
    
    def find_middle(self):
        middle_point = self.head
        end_point = self.head

        while end_point is not None and end_point.get_next() is not None:
            middle_point = middle_point.get_next()
            end_point = end_point.get_next().get_next()

        return middle_point.get_value()