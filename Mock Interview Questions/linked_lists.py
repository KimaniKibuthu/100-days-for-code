class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head()
        while itr:
            count += 1
            itr = itr.next
        
        return count

    def remove_at_idx(self, idx):
        if idx < 0 or idx >= self.get_length():
            raise Exception('invalid index')
        
        if idx == 0:
            self.head = self.head.next
        
        count = 0
        itr = self.head
        while itr:
            if count == idx - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at_idx(self, idx, data):
        if idx < 0 or idx >= self.get_length():
            raise Exception('invalid index')
        
        if idx == 0:
            self.insert_at_beginning(data)
        
        count = 0
        itr = self.head
        while itr:
            if count == idx - 1:
                node = Node(data, itr.next)
                itr.next = node
            itr = itr.next
            count += 1

    
    def print(self):
        if self.head is None:
            print('The Linked list is empty')
        
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        
        print(llstr)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(76)
    ll.insert_at_beginning(56)
    ll.insert_at_beginning(98)
    ll.print()