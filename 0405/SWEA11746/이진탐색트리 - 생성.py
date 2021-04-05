import sys
sys.stdin = open('input.txt')

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root == Node(value)

        else:
            self.current_node = self.root
            while True:
                if value > self.current_node.value:
                    if self.current_node.left == None:
                        self.current_node.left = Node(value)
                        break
                    else:
                        self.current_node = self.current_node.left
                else:
                    if self.current_node.right == None:
                        self.current_node.right = Node(value)
                        break
                    else:
                        self.current_node = self.current_node.right