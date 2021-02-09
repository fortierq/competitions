# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def f(t, acc):
            if t is None:
                return None, 0
            d, totd = f(t.right, acc)
            r = t.val + acc + (0 if d is None else totd)
            g, totg = f(t.left, r)
            return TreeNode(r, g, d), totg + totd + t.val
        return f(root, 0)[0]