# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode):
        traversal = {}
        prof =  {}
        def f(node, pos, p):
            prof[node.val] = p
            if pos not in traversal:
                traversal[pos] = []
            traversal[pos].append(node.val)
            if node.left:
                f(node.left, pos - 1, p + 1)
            if node.right:
                f(node.right, pos + 1, p + 1)

        f(root, 0, 0)
        mini, maxi = min(traversal), max(traversal)
        res = []
        for i in range(mini, maxi + 1):
            res.append(sorted(traversal[i], key=lambda x: (prof[x], x)))
        return res

def valid_node(L, j):
    return j < len(L) and L[j]

def list_to_tree(L, i):
    n = len(L)
    left = None
    if valid_node(L, 2 * i + 1):
        left = list_to_tree(L, 2 * i + 1)
    right = None
    if valid_node(L, 2 * i + 2):
        right = list_to_tree(L, 2 * i + 2)
    return TreeNode(L[i], left, right)

S = Solution()
L = list_to_tree([0,5,1,9,None,2,None,None,None,None,3,4,8,6,None,None,None,7], 0)
print(S.verticalTraversal(L))