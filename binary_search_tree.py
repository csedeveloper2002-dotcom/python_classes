
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)


    def search(self, root, key):
        if root is None or root.data == key:
            return root
        if key < root.data:
            return self.search(root.left, key)
        return self.search(root.right, key)


bst = BST()
values = [50, 30, 70, 20, 40, 60, 80]

for v in values:
    bst.root = bst.insert(bst.root, v)

print("Inorder Traversal:")
bst.inorder(bst.root)

key = 40
if bst.search(bst.root, key):
    print(f"\n{key} found in BST")
else:
    print(f"\n{key} not found in BST")
