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
    
    def insert_at_end(self, data):
        if self.head is None:     #if our linked list is empty the direct inset 
            self.head = Node(data)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)
    
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index!")
        
        if index == 0:
            self.insert_at_begining(data)
            return
        
        itr = self.head
        cnt = 0
        while itr:
            if cnt == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            cnt += 1
            
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

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
root.insert_at_begining(15)
root.insert_at_end(4)
root.insert_at_end(3)
root.insert_at(0, 1000)
root.insert_at(10, 1000)
print(root.get_length())
root.print()
