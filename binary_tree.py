class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child is None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, value):
        if self.right_child is None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node

    def pre_order(self):
        print(self.value)

        if self.left_child:
            self.left_child.pre_order()

        if self.right_child:
            self.right_child.pre_order()

    def in_order(self):
        if self.left_child:
            self.left_child.in_order()

        print(self.value)

        if self.right_child:
            self.right_child.in_order()

    def post_order(self):
        if self.left_child:
            self.left_child.post_order()

        if self.right_child:
            self.right_child.post_order()

        print(self.value)


if __name__ == "__main__":
    node2 = BinaryTree(2)
    node2.insert_left(7)
    node2.insert_right(5)

    node7 = node2.left_child
    node7.insert_left(2)
    node7.insert_right(6)

    node6 = node7.right_child
    node6.insert_left(5)
    node6.insert_right(11)

    node5 = node2.right_child
    node5.insert_right(9)

    node9 = node5.right_child
    node9.insert_left(4)

    # node2.pre_order()
    # node2.in_order()
    node2.post_order()
