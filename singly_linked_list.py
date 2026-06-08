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
    
    def get_length(self):
        i , current = 0, self.head
        while current is not None:
            i += 1
            current = current.next
        return i
    
    def mid_node(self):
        if self.head is None:
            return
        fast, slow = self.head, self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow.value

    def search(self, target):
        current = self.head
        while current is not None:
            if current.value == target:
                return True
            current = current.next
        return False

    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev
        
        

linked = SinglyLinkedList()
print("Existe : ", linked.search(5))
linked.insert_end(5)
linked.insert_end(8)
linked.insert_end(9)
linked.insert_end(10)
# linked.delete_end()
print("Existe : ", linked.search(5))
print("Tile : ", linked.get_length())
print("Middle : ", linked.mid_node())

linked.display()
linked.reverse()
linked.display()