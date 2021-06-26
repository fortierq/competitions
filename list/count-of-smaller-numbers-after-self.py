import random

class BST:
    def __init__(self):
        self.root = None

    def add(self, x):
        if not self.root:
            self.root = Node(x)
        else:
            self.root.add(Node(x))

    def numSmaller(self, x):
        def find(node):
            if not node: return 0
            if node.val < x:
                res = 1
                if node.left:
                    res += node.left.sz
                return res + find(node.right)
            elif node.val == x:
                res = 0
                if node.left:
                    res += node.left.sz
                return res
            return find(node.left)

        return find(self.root)

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.sz = 1

    def add(self, node):
        self.sz += 1
        if node.val < self.val:
            if self.left:
                self.left.add(node)
            else:
                self.left = node
        else:
            if self.right:
                self.right.add(node)
            else:
                self.right = node

class Solution:
    def countSmaller(self, nums):
        bst = BST()
        n = len(nums)
        res = [0 for i in range(n)]
        for i in range(n)[::-1]:
            res[i] = bst.numSmaller(nums[i])
            bst.add(nums[i])
        return res
