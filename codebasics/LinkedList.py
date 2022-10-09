class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init(self):
        self.head = None

    def get_length(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def insert_at_begining(self, data):
        node = Node(data, None)
        self.head = node

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

        if index == 0:
            self.insert_at_begining(data)

        count = 0
        curr = self.head

        while curr:
            if count == index - 1:
                node = Node(data, curr.next)
                curr.next = node
                break
            curr = curr.next
            count += 1

    def remove_at_index(self, index):
        if index < 0 and index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        curr = self.head
        while curr:
            if count == index - 1:
                curr.next = curr.next.next
                break
            curr = curr.next
            count += 1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        curr = self.head
        llstr = ''
        while curr:
            llstr += str(curr.data) + ' --> ' if curr.next else str(curr.data)
            curr = curr.next
        print(llstr)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(['banana', 'apple', 'pawpaw', 'mangoes'])
    ll.insert_at_index(2, 'figs')
    ll.remove_at_index(3)
    ll.print()