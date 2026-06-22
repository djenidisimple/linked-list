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
           self.put_prefixe(current_node.left, data)
           self.put_prefixe(current_node.right, data) 
    
    def put_postfixe(self, current_node, data):
        if current_node is not None:
           self.put_postfixe(current_node.left, data)
           self.put_postfixe(current_node.right, data) 
           data.append(current_node.value) 
    
    def search(self, value):
        if self.root is None:
            return False
        current = self.root
        while current is not None:
            if current.value == value:
                return True
            elif current.value > value:
                current = current.left
            else:
                current = current.right
        return False
    
    def delete(self, value):
        if self.root is None:
            return
        parent = None
        current = self.root
        while current is not None and current.value != value:
            parent = current
            if current.value > value:
                current = current.left
            else:
                current = current.right
        
        if current is None:
            return
        
        if current.left is None:
            child = current.left
        elif current.right is None:
            child = current.right
        else:
            pass
        
        if parent is None:
            self.root = child
        elif parent.left == value:
            parent.left = child
        else:
            parent.right = child
            
'''
          15
        /    \
      10     20
     /  \    / \
    8   12  17 25
          15
        /    \
      10     17
     /  \      \
    8   12      25
'''
tree = BST()
data = [15, 10, 20, 8, 12, 17, 25]
for x in data:
    tree.insert(x)
print("Données initiales :", data)
print("Parcours Infixe   :", tree.depth_infixe())
print("Parcours Prefixe   :", tree.depth_prefixe())
print("Parcours Postfixe   :", tree.depth_postfixe())
print("Est ce que 15 est dans la liste : ", tree.search(1))