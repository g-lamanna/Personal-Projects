class TreeNode:

    def __init__(self,value,name):
        self.value = value
        self.name = name
        self.children = []
        self.parent = None

    def add_child(self,child_node):
        child_node.parent = self
        self.children.append(child_node)
    
    def remove_child(self,child_node):
        self.children = [i for i in self.children if i != child_node]
    
    def get_depth(self):
        size = 0
        p = self.parent
        while p:
            size += 1
            p = p.parent
        return size
    
    def print_tree(self,level=None):
        if self.get_depth() > level:
            return
        spaces = " " * self.get_depth() * 3
        print(spaces+str(self.value)+" "+str(self.name))
        if self.children:
            for child in self.children:
                child.print_tree(level)
    
    
root = TreeNode("Projects","Directory")

stack=TreeNode("Stack","Folder")
stack_2 = TreeNode("Stack-2","file")

stack.add_child(TreeNode("Stack-1","file"))
stack.add_child(stack_2)
stack.add_child(TreeNode("Stack-3","file"))

cs=TreeNode("CS-50","Folder")
cs.add_child(TreeNode("cs-1","file"))
cs.add_child(TreeNode("cs-2","file"))
cs.add_child(TreeNode("cs-3","file"))

build = TreeNode("Mars","Build-File")
stack_2.add_child(build)




root.add_child(cs)
root.add_child(stack)
# chiron.add_child(tree)
# stack.add_child(tower)
# stack.add_child(node)
# tree.add_child(hierarchy)

print(root.print_tree(3))