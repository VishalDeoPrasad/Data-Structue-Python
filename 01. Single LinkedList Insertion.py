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
    
    def insert_value(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def remove_at(self, index):
        #first validate the index value
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index!")
        
        if index == 0:
            self.head = self.head.next
            return
        
        cnt = 0
        itr = self.head
        while itr:
            if cnt == index - 1:
                itr.next = itr.next.next
                break

            cnt += 1
            itr = itr.next

    def remove_by_value(self, val):
        if self.get_length() == 0:
            raise Exception("LinkedList is Empty!")

        itr = self.head
        index = 0
        while itr:
            if itr.data == val:
                self.remove_at(index)
                print(itr.data, index)
                break
            itr = itr.next
            index += 1

    def insert_after_value(self, val, data):
        if self.get_length() == 0:
            raise Exception("LinkedList is Empty!")
        
        itr = self.head
        index = 0
        while itr:
            if itr.data == val:
                itr.next = Node(data, itr.next)
            itr = itr.next
            index += 1

root = linked_list()
# root.insert_at_begining(5)
# root.insert_at_begining(10)
# root.insert_at_begining(15)
# root.insert_at_end(4)
# root.insert_at_end(3)
# root.insert_at(4, 1000)

root.insert_value(["A", "B", "C", "D"])
# root.remove_at(2)
# root.insert_at(2, "Cata")
print(root.get_length())
#root.remove_by_value("B")
root.insert_after_value("D
", "E")
root.print()
