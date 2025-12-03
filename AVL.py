class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVL:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        return node.height if node else 0

    def update_height(self, node):
        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        x = y.left
        t = x.right
        x.right = y
        y.left = t
        self.update_height(y)
        self.update_height(x)
        return x

    def left_rotate(self, x):
        y = x.right
        t = y.left
        y.left = x
        x.right = t
        self.update_height(x)
        self.update_height(y)
        return y

    def rebalance(self, node):
        self.update_height(node)
        balance = self.get_balance(node)

        if balance > 1:
            if self.get_balance(node.left) < 0:
                node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance < -1:
            if self.get_balance(node.right) > 0:
                node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if not node:
            return Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            return node

        return self.rebalance(node)

    def get_tree_height(self):
        return self.get_height(self.root)