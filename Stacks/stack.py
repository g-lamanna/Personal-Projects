from node import Node

class Stack:

    #initializes class attribures for instances of Stack object
    def __init__(self,name,limit=100):
        #self.name = name
        self.limit = limit
        self.head_node = None
        self.size = 0
        self.name = name
    
    #places node at head of stack
    def push(self,value_to_add):
        if self.has_space():
            self.value_to_add = value_to_add
            current_node = Node(self.value_to_add)
            current_node.set_next_node(self.head_node)
            self.head_node = current_node
            self.size += 1
        else:
            print("No more space in line for {}!".format(self.value_to_add))

    #removes node from top of stack and returns that node's value
    def pop(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            value_to_remove = self.head_node
            self.head_node = value_to_remove.get_next_node()
            self.size -= 1
            return value_to_remove.get_value()

    #retrieves value from head node
    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            return self.head_node.get_value()

    #returns size of stack
    def get_size(self):
        return self.size
    #checks if stack is empty
    def is_empty(self):
        return self.size == 0

    #checks if stack has enough space for more nodes
    def has_space(self):
        return self.limit > self.size
    
    #return name of stack
    def get_name(self):
        return self.name
    
    def print_items(self):
        pointer = self.head_node
        pointer_list = []
        while pointer:
            pointer_list.append(pointer.get_value())
            pointer = pointer.get_next_node()
        pointer_list.reverse()
        print("{}:{}".format(self.get_name(),pointer_list))