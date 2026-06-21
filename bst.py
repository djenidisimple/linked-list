class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    break
                else:
                    current = current.right
    
    def depth_infixe(self):
        if self.root is None:
            return
        data = []
        self.put_infixe(self.root, data)
        return data
    
    def depth_prefixe(self):
        if self.root is None:
            return
        data = []
        self.put_prefixe(self.root, data)
        return data
    
    def depth_postfixe(self):
        if self.root is None:
            return
        data = []
        self.put_postfixe(self.root, data)
        return data
    
    def put_infixe(self, current_node, data):
        if current_node is not None:
           self.put_infixe(current_node.left, data)
           data.append(current_node.value) 
           self.put_infixe(current_node.right, data) 

    def put_prefixe(self, current_node, data):
        if current_node is not None:
           data.append(current_node.value) 
           self.put_infixe(current_node.left, data)
           self.put_infixe(current_node.right, data) 
    
    def put_postfixe(self, current_node, data):
        if current_node is not None:
           self.put_infixe(current_node.left, data)
           self.put_infixe(current_node.right, data) 
           data.append(current_node.value) 

tree = BST()
data = [15, 10, 20, 8, 12, 17, 25]
for x in data:
    tree.insert(x)
print("Données initiales :", data)
print("Parcours Infixe   :", tree.depth_infixe())
print("Parcours Prefixe   :", tree.depth_prefixe())
print("Parcours Postfixe   :", tree.depth_postfixe())