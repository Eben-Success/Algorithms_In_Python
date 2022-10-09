class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

        def print(self):
            if self.head is None:
                print("Linked list is empty")
                return
            itr = self.head
            llstr = ''
            while itr:
                llstr += str(data) + '-->' if itr.next else str(itr.data)
                itr = itr.next
            print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count
