from Node import Node

class LinkedList:
    def __init__(self):
        self.head_node = None
    
    def get_head(self):
        return self.head_node
    
    def is_empty(self):
        if(self.head_node is None):
            return True
        else:
            return False
    
    def insert_at_head(self, dt):
        temp_node = Node(dt)
        if self.is_empty():
            self.head_node = temp_node
            return self.head_node
        
        temp_node.next_element = self.head_node
        self.head_node = temp_node
        return self.head_node