class Node:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, value):
        if self.head is None:
            self.head = Node(value, None, None)
        else:
            new_node = Node(value, None, self.head)
            self.head.prev = new_node
            self.head = new_node

    def insert_end(self, value):
        if self.head is None:
            self.head = Node(value, None, None)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value, current, None)
    
    def delete_begin(self):
        if self.head is not None:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
    
    def delete_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None 
        
    def display(self):
        if self.head is None:
            return
        current = self.head
        while current.next is not None:
            print(current.value, end=" , ")
            current = current.next
        print(current.value)
    
    def display_reverse(self):
        if self.head is None:
            return
        current = self.head
        while current.next is not None:
            current = current.next
        while current.prev is not None:
            print(current.value, end=" , ")
            current = current.prev
        print(current.value)

        
linked = DoublyLinkedList()
linked.insert_end(5)
linked.insert_end(8)
linked.display()
linked.display_reverse()