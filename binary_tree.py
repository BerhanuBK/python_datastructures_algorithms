# Implement Binary Tree using Pyhton
class Tree:
    left  = None
    right = None
    value = None
    
    def __init__(self, val):
        if val != None:
            self.value = val
        self.left  = None
        self.right = None
        
    def insert(self, val):
        if self.value:
            if val < self.value:
                if self.left is None:
                    self.left = Tree(val)
                else:
                    self.left.insert(val) 
                   
            if val > self.value:
                if self.right is None:
                    self.right = Tree(val)
                else:
                    self.right.insert(val)
        else:
            self.value = val
            
    def display(self):
        if self.left:
            self.left.display()
        print(self.value)
        if self.right:
            self.right.display()
        
tree_object = Tree(20)
#ree_object.display()

tree_object.left  = Tree(18)
tree_object.right = Tree(22)

#rint(tree_object.left.value)
#rint(tree_object.right.value)

tree_object.insert(12)
tree_object.insert(19)
tree_object.insert(24)
tree_object.insert(5)
tree_object.insert(21)
tree_object.display()
