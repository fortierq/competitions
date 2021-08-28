# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        cur, nex = [root], []
        cur2 = cur[:]
        while True:
            v = cur.pop()
            if v.left:
                nex.append(v.left)
            if v.right:
                nex.append(v.right)
            if not cur:
                if not nex:
                    return sum(w.val for w in cur2)
                cur = nex[:]
                nex = []
                cur2 = cur[:]
