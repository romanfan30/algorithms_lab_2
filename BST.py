from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def getheight(self, node=None):
        if node is None:
            node = self.root
            if node is None:
                return 0
        if node.left is None and node.right is None:
            return 1
        left_height = self.getheight(node.left) if node.left else 0
        right_height = self.getheight(node.right) if node.right else 0
        return 1 + max(left_height, right_height)

    def search(self, value):
        current = self.root
        while current is not None:
            if value == current.value:
                return current.value
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_recursive(self.root, value)

    def insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self.insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self.insert_recursive(current.right, value)

    def delete(self, value):
        parent = None
        current = self.root

        while current is not None and current.value != value:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        if current is None:
            return

        if current.left is None and current.right is None:
            if parent is None:
                self.root = None
            elif parent.left == current:
                parent.left = None
            else:
                parent.right = None

        elif current.left is not None and current.right is not None:
            min_parent = current
            min_node = current.right
            while min_node.left is not None:
                min_parent = min_node
                min_node = min_node.left

            current.value = min_node.value

            if min_parent == current:
                min_parent.right = min_node.right
            else:
                min_parent.left = min_node.right

        else:
            child = current.right if current.right is not None else current.left

            if parent is None:
                self.root = child
            elif parent.left == current:
                parent.left = child
            else:
                parent.right = child

    def maximum(self, current):
        if current.right is None:
            return current.value
        return self.maximum(current.right)

    def minimum(self, current):
        if current.left is None:
            return current.value
        return self.minimum(current.left)

    def traverse_straight(self, current):
        if current is not None:
            print(current.value, end=" ")
            self.traverse_straight(current.left)
            self.traverse_straight(current.right)

    def traverse_centred(self, current):
        if current is not None:
            self.traverse_centred(current.left)
            print(current.value, end=" ")
            self.traverse_centred(current.right)

    def traverse_back(self, current):
        if current is not None:
            self.traverse_back(current.left)
            self.traverse_back(current.right)
            print(current.value, end=" ")

    def traverse_wide(self, current):
        if current is None:
            return
        queue = deque()
        queue.append(current)
        while queue:
            node = queue.popleft()
            print(node.value, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)