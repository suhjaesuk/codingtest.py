class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head=None
        self.tail=None

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next=new_node
            self.tail=self.tail.next

    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value

    def insert(self,value,idx):
        current = self.head
        new_node = Node(value)
        for i in range(idx):
            current=current.next
        current = new_node
        new_node = current.next
        return None



list = LinkedList()
list.append(1)
list.append(2)
list.insert(100,1)

print(list.get(1))