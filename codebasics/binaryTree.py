class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def add_child(self, data):
        if data == self.data:
            return  # node already exist
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
            elements += self.left.in_order_traversal()
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum


def build_tree(elements):
    print("Building tree with these elements: ", elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


if __name__ == '__main__':
    numbers_tree = build_tree([17, 2, 35, 3, 56, 5, 33, 5, 26, 7, 43])
    print("In order traversal gives this sorted list: ", numbers_tree.in_order_traversal())
    print("Max ", numbers_tree.find_max())
    print("Min ", numbers_tree.find_min())
    print("Sum ", numbers_tree.calculate_sum())
    print("Pre order traversal: ", numbers_tree.pre_order_traversal())
    print("Post order traversal: ", numbers_tree.post_order_traversal())
