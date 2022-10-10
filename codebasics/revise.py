class Node:
    def __init(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, None)
        self.head = node

    def get_length(self):
        count = 0
        curr = self.head

        while curr:
            count += 1
            curr = curr.next
        return count

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data, None)

    def insert_at_index(self, index, data):
        if index < 0 and index > self.get_length():
            raise Exception("Invalid Index")

        count = 0
        curr = self.head

        while curr:
            if count == index - 1:
                curr.next = curr.next.next
                break
            curr = curr.next
            count +=1

    def insert_value(self, data_lisit):
        self.head = None
        for data in data_list:
            self.insert_at_beginning(data)



