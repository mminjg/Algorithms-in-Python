import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return

        node = self.root
        pre_node = None
        while node:
            pre_node = node
            if data < node.data:
                node = node.left
            elif data > node.data:
                node = node.right

        if data < pre_node.data:
            pre_node.left = new_node
        else:
            pre_node.right = new_node

    def postorder(self, node):
        if not node.left == None:
            self.postorder(node.left)
        if not node.right == None:
            self.postorder(node.right)
        print(node.data)

tree = BinaryTree()
while True:
    try:
        data = int(input())
        tree.insert(data)
    except:
        break

tree.postorder(tree.root)