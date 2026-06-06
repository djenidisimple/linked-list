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
            self.head.prev = self.head
            self.head.next = self.head
            return
        last_node = self.head.prev
        new_node = Node(value, self.head.prev, self.head)
        self.head.prev = new_node 
        last_node.next = new_node
        self.head = new_node
    
    def insert_end(self, value):
        if self.head is None:
            self.head = Node(value, None, None)
            self.head.prev = self.head
            self.head.next = self.head
            return
        last_node = self.head.prev
        new_node = Node(value, last_node, self.head)
        self.head.prev = new_node
        last_node.next = new_node
    
    def delete_begin(self):
        if self.head is None:
            return
        
        if self.head.next == self.head:
            self.head = None
            return
        
        last_node = self.head.prev
        new_head = self.head.next
        new_head.prev = last_node
        last_node.next = new_head
        self.head = new_head 
    
    def delete_end(self):
        if self.head is None:
            return
        if self.head.next == self.head:
            self.head = None
            return
        
        new_last_node = self.head.prev.prev
        new_last_node.next = self.head
        self.head.prev = new_last_node
    
    def display(self):
        if self.head is None:
            return
        current = self.head
        while current.next != self.head:
            print(current.value, end=" -> ")
            current = current.next
        print(current.value)

linked = DoublyLinkedList()
linked.insert_end(5)
linked.insert_end(8)
linked.insert_end(9)
linked.insert_end(10)
linked.delete_end()
linked.delete_end()
linked.display()
        