class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class linked_list:
    def __init__(self):
        self.head = None #crate a empty linked List and later we will insert node to this linked list
    
    def insert_at_begining(self, data):
        node = Node(data, self.head) #create the node and give data and 
        self.head = node

    def print(self):
        itr = self.head
        llist = ""
        while itr:
            llist += str(itr.data) + "-->"
            itr = itr.next
        print(llist)

root = linked_list()
root.insert_at_begining(5)
root.insert_at_begining(10)
root.print()
