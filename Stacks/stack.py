from node import Node

class Stack:

    #Initializes class attribures for instances of Stack object
    def __init__(self,limit=100):
        #self.name = name
        self.limit = limit
        self.head_node = None
        self.size = 0
    
    #Places node at head of stack
    def push(self,value_to_add):
        if self.has_space():
            self.value_to_add = value_to_add
            current_node = Node(self.value_to_add)
            current_node.set_next_node(self.head_node)
            self.head_node = current_node
            self.size += 1
            print("{} just entered line".format(self.value_to_add))
        else:
            print("No more space in line for {}!".format(self.value_to_add))

    #Removes node from top of stack and returns that node's value
    def pop(self):
        if self.is_empty():
            print("Nobody in line!")
        else:
            value_to_remove = self.head_node
            self.head_node = value_to_remove.get_next_node()
            self.size -= 1
            print("{} left the line".format(value_to_remove.get_value()))
            return value_to_remove.get_value()

    #Retrieves value from head node
    def peek(self):
        if self.is_empty():
            print("Nobody is in line!")
        else:
            return self.head_node.get_value()
            

    #help to check if stack is empty
    def is_empty(self):
        return self.size == 0

    #helperto check if stack has enough space for more nodes
    def has_space(self):
        return self.limit > self.size
    
    #helper to return name of stack
    def get_name(self):
        return self.name
    
print("The Line is open!")

stack = Stack(6)

stack.push("Gary")
stack.push("Tom")
stack.push("Sarah")
stack.push("Molly")
stack.push("Greg")
stack.push("Byron")

stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
