class Node:

    #Initializes node class attributes for new instances of Node class
    def __init__(self,value,next_node=None):
        self.value = value 
        self.next_node = next_node

    #returns value of node
    def get_value(self):
        return self.value 
    
    #returns the next node in the list 
    def get_next_node(self):
        return self.next_node
    
    #sets the node
    def set_next_node(self,next_node):
        self.next_node = next_node


