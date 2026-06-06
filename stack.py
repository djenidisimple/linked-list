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
    
    def peek(self):
        if self.head is None:
            return
        print(self.head.value)

stack = Stack()
stack.push(5)
stack.push(8)
# stack.pop()
stack.peek()