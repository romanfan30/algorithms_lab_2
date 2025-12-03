class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.is_red = True


class RB:
    def __init__(self):
        self.root = None

    def rotate_left(self, x):
        y = x.right
        x.right = y.left

        if y.left:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def rotate_right(self, x):
        y = x.left
        x.left = y.right

        if y.right:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            self.root.is_red = False
            return

        new_node = self._bst_insert(self.root, value)
        self.fix_insert(new_node)

    def _bst_insert(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
                current.left.parent = current
                return current.left
            return self._bst_insert(current.left, value)

        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
                current.right.parent = current
                return current.right
            return self._bst_insert(current.right, value)

        return current

    def fix_insert(self, z):
        while z != self.root and z.parent.is_red:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right

                if y and y.is_red:
                    z.parent.is_red = False
                    y.is_red = False
                    z.parent.parent.is_red = True
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.rotate_left(z)

                    z.parent.is_red = False
                    z.parent.parent.is_red = True
                    self.rotate_right(z.parent.parent)
            else:
                y = z.parent.parent.left

                if y and y.is_red:
                    z.parent.is_red = False
                    y.is_red = False
                    z.parent.parent.is_red = True
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.rotate_right(z)

                    z.parent.is_red = False
                    z.parent.parent.is_red = True
                    self.rotate_left(z.parent.parent)

        self.root.is_red = False

    def get_tree_height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0

        left_height = self._height(node.left)
        right_height = self._height(node.right)

        return max(left_height, right_height) + 1