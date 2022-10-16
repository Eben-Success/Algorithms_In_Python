class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist
        else:
            if data < self.data:
                if self.left:
                    self.left.add_child(data)
                else:
                    self.left = BinarySearchTreeNode(data)
            else:
                if data > self.data:
                    if self.right:
                        self.right.add_child(data)
                    else:
                        self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.left:
            # might be in the left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.right:
            # might be in the right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_oder_traversal()
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

def build_tree(elements):
    print("Building tree with these elements: ", elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements))


