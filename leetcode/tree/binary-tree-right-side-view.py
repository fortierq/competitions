#  https://leetcode.com/problems/binary-tree-right-side-view/
#  Can also use BFS 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode):
        d = {}

        def dfs(v, prof):
            if v:
                if prof not in d:
                    d[prof] = v.val
                dfs(v.right, prof + 1)
                dfs(v.left, prof + 1)

        dfs(root, 0)
        return [d[i] for i in range(len(d))]


s = Solution()
t = TreeNode(1, TreeNode(2, None, TreeNode(3, None, None)), TreeNode(4, None, None))
print(s.rightSideView(t))
