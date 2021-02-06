#  https://leetcode.com/problems/binary-tree-right-side-view/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode):
        d = {}

        def f(v, prof, pos):
            if v:
                if prof not in d or d[prof][0] < pos:
                    d[prof] = (pos, v.val)
                f(v.right, prof + 1, 2 * pos + 1)
                f(v.left, prof + 1, 2 * pos)

        f(root, 0, 0)
        L = list(d.values())
        try:
            return list(zip(*L))[1]
        except:
            return []


s = Solution()
t = TreeNode(1, TreeNode(2, None, TreeNode(3, None, None)), TreeNode(4, None, None))
print(s.rightSideView(t))
