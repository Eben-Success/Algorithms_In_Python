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
        if index < 0 and index > self.get_length():
            raise Exception("Invalid Exception")

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        curr = self.head
        while curr:
            if count == index - 1:
                node = Node(data, self.next)
                curr.next = node
                break
            curr = curr.next
            count += 1

    def remove_at_index(self, index):
        if index < 0 and index > self.get_length():
            raise Exception("Invalid Exception")

        if index == 0:
            self.head = self.head.next

        count = 0
        curr = self.head
        while curr:
            if count == index - 1:
                curr.next = curr.next.next
                break

            curr = curr.next
            count += 1

