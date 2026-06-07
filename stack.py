class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
    
    def pop(self):
        if self.head is None:
            return
        
        self.head = self.head.next
        return self.head.value
    
    def isEmpty(self):
        return self.head is None
    
    def peek(self):
        if self.head is None:
            return
        print(self.head.value)

stack = Stack()
print("isEmpty : ", stack.isEmpty())
stack.push(5)
stack.push(8)
print("isEmpty : ", stack.isEmpty())
# stack.pop()
stack.peek()