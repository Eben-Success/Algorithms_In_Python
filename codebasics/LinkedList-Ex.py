class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init(self):
        self.head = None


    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def get_length(self):
        count = 0
        curr = self.next

        while curr:
            count += 1
            curr = curr.next
        return count

    def insert_at_index(self, index, data):

