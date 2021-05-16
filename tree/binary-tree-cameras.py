# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
        
    def minCameraCover(self, s: TreeNode) -> int:
        cur = set()
        pred = dict()
        cover = set()
        def aux(v):
            is_leaf = True 
            for child in [v.left, v.right]:
                if child is not None:
                    is_leaf = False
                    pred[id(child)] = id(v)
                    aux(child)
            if is_leaf:
                cur.add(id(v))
        aux(s)
        def effeuiller():
            nonlocal cur, cover
            cur2 = set()
            for c in cur:
                if c in pred and pred[c] not in cover:
                    cover.add(pred[c])
                    cur2.add(pred[c])
            cur = cur2
            print(cur)
            
        res = 0
        effeuiller()
        while cur:
            res += len(cur)
            effeuiller()
            effeuiller()
        return res
