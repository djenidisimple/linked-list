class Node:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
    
    def enqueue(self, value):
        if self.head is None:
            self.head = Node(value, None, None)
            self.head.next = self.head
            self.head.prev = self.head
            return
        last_node = self.head.prev
        new_node = Node(value, last_node, self.head)
        last_node.next = new_node
        self.head.prev = new_node
    
    def dequeue(self):
        if self.head is None:
            return
        
        popped_value = self.head.value
        
        if self.head.next is None:
            self.head = None
            return popped_value
        last_node = self.head.prev
        new_node = self.head.next
        last_node.next = new_node
        new_node.prev = last_node
        self.head = new_node 
        return popped_value
    
    def display(self):
        if self.head is None:
            return
        current = self.head
        while current.next != self.head:
            print(current.value)
            current = current.next
        print(current.value)

q = Queue()
q.enqueue(10) # Premier arrivé
q.enqueue(20)
q.enqueue(30) # Dernier arrivé
print("File initiale :")
q.display() # 10 <- 20 <- 30

print("\nDébut du service (dequeue) :")
print("Servi :", q.dequeue()) # Doit sortir 10 (Premier arrivé, premier servi)
print("File restante :")
q.display()
