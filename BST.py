from Node import Node

class BinarySearchTree:

    def __init__(self, root_value):
        self.root = Node(root_value)

    def add_node(self, value, node=None):
        if not node:
            node = self.root #we have a node, its 100
        if value > node.value: # more than 70 no
            if not node.right: #skip
                node.right = Node(value)
            else: 
                return self.add_node(value, node.right)
        else:
            if not node.left: #now here - continue
                node.left = Node(value)
                return
            else:
                return self.add_node(value, node.left)
                

    def get_min(self, node=None):
        if not node:
            node = self.root
        if node.left:
            return self.get_min(node.left)    
        else:
            return node.value

    def get_max(self, node=None):
        if not node:
            node = self.root
        if node.right:
            return self.get_max(node.right)
        else:
            return node.value
        
    def get_max_loop(self):
        node = self.root
        while node.right:
            node = node.right
        return node.value


    def contains(self, target): #if this # is in there, find nothing we return false
        current_node = self.root
        while current_node:
            if target == current_node.value:
                return True
            if target > current_node.value:
                current_node = current_node.right
            else:    
                current_node = current_node.left
        return False

    def print_in_order(self, node=None): #maintains sorted order, take node in firs step
        if not node:
            node = self.root
        if node:
            if node.left:
                self.print_in_order(node.left)
            print(node.value)
            if node.right:
                self.print_in_order(node.right)
            

    #test as we go
bst = BinarySearchTree(100)
bst.add_node(80)
bst.add_node(90)
bst.add_node(85)
bst.add_node(150)
# print(bst.root.left.right.value) #90
# print(bst.root.left.right.right.value) #85

#print(bst.get_min()) #80 its recursive bcuz we are calling the method - ex. get in in get in
#print(bst.get_max())

# print(bst.contains(110)) #False
# print(bst.contains(90))  #True
# print(bst.contains(150)) #True
# print(bst.contains(200)) #False

bst.print_in_order()
#80
# 85
# 90
# 100
# 150