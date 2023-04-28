from Node import Node

class BinarySearchTree:

    def __init__(self, root_value):
            self.root = Node(root_value)

    def bst_decorator(func): 
        def wrapper(alist):
            # root_value = None
            # for item in alist:
            #     root_value = add_node(root_value, item) 
            result = func(alist)
            return result
        return wrapper

    def add_node(self, value, node=None):
            if not node:
                node = self.root 
            if value > node.value: 
                if not node.right: 
                    node.right = Node(value)
                else: 
                    return self.add_node(value, node.right)
            else:
                if not node.left: 
                    node.left = Node(value)
                    return
                else:
                    return self.add_node(value, node.left)
               
    @bst_decorator 
    def list_to_bts_value(alist):
        Node = None
        for item in alist:
              Node = add_node(value, node=None)
        return Node
            # if n < 2:
            #     return 1
            # return value(n-1) + value(n-2)
    #     if n == 0:
    #          return 1
    #     return 
    # #bts_value(100)
# bst = BinarySearchTree(2)            

input_list = [33,44,2,77,18,99]
result = (input_list)
print(result)