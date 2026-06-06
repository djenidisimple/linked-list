class Node:
    def __init__(self, value, next):
        self.value = value 
        self.next = next

class CircularLinkedList:

    def __init__(self):
        self.head = None 
    
    def insert_begin(self, value):
        if self.head is None:
            self.head = Node(value, None)
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            new_node = Node(value, self.head)
            current.next = new_node
            self.head = new_node
    
    def insert_end(self, value):
        if self.head is None:
            self.head = Node(value, None)
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = Node(value, self.head)
    
    def delete_begin(self):
        if self.head is None:
            return
        if self.head.next == self.head:
            self.head = None
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = self.head.next
        self.head = self.head.next
    
    def delete_end(self):
        if self.head is None:
            return
        if self.head.next == self.head:
            self.head = None
            return
        current = self.head
        while current.next.next != self.head:
            current = current.next
        current.next = self.head
    
    def display(self):
        if self.head is None:
            return
        else:
            current = self.head
            while current.next != self.head:
                print(current.value, end=" -> ")
                current = current.next
            print(current.value)

linked = CircularLinkedList()
linked.insert_begin(5)
linked.insert_begin(8)
linked.insert_begin(9)
linked.insert_begin(10)
# linked.delete_end()
linked.display()
