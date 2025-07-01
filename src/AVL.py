#data structure for users
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 0  # New node is initially added at leaf

class AVLTree:
    def __init__(self):
        self.root = None

    # Get height of node
    def _get_height(self, node):
        pass

    # Get balance factor
    def _get_balance(self, node):
        pass

    # Right rotate
    def _right_rotate(self, z):
        pass

    # Left rotate
    def _left_rotate(self, z):
        pass

    # Insert a key into the subtree rooted with node and return new root
    def _insert(self, node, key):
        pass

    # Public method to insert key
    def insert(self, key):
        self.root = self._insert(self.root, key)

    # Inorder traversal (for testing and visualization)
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.key, end=' ')
            self.inorder_traversal(node.right)

    def print_inorder(self):
        self.inorder_traversal(self.root)
        print()
