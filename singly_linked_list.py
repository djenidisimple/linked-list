# Singly Linked List
class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def insert_begin(self, value):
        self.head = Node(value, self.head)
    def insert_end(self, value):
        if self.head is None:
            self.head = Node(value, self.head)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            new = Node(value, None)
            current.next = new
    def display(self):
        current = self.head
        while current.next is not None:
            print(current.value, end=" -> ")
            current = current.next    
        print(current.value)
    def delete_begin(self):
        self.head = self.head.next 
    def delete_end(self):
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None
linked = SinglyLinkedList()
linked.insert_end(5)
linked.insert_end(8)
linked.insert_end(9)
linked.insert_end(10)
linked.delete_end()
linked.display()