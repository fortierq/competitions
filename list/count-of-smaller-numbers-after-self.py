class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self, nums):
        self.nums = nums
        self.tree = None
        if self.nums:
            self.tree = self._build(0, len(self.nums)-1)
    
    def _build(self, start, end):
        node = Node()
        if start == end:
            node.val = self.nums[start]
            return node
        mid = (start + end) // 2
        left = self._build(start, mid)
        right = self._build(mid+1, end)
        node.val = left.val + right.val
        node.left, node.right = left, right
        return node
    
    def update(self, idx, val):
        self._update(self.tree, 0, len(self.nums)-1, idx, val)
    
    def _update(self, node, start, end, idx, val):
        if start == end:
            self.nums[idx] += val
            node.val += val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self._update(node.left, start, mid, idx, val)
            else:
                self._update(node.right, mid+1, end, idx, val)
            node.val = node.left.val + node.right.val
    
    def query(self, i, j):
        return self._query(self.tree, 0, len(self.nums)-1, i, j)
    
    def _query(self, node, start, end, l, r):
        if start > r or end < l:
            return 0
        if l <= start and end <= r:
            return node.val
        mid = (start + end) // 2
        q1 = self._query(node.left, start, mid, l, r)
        q2 = self._query(node.right, mid+1, end, l, r)
        return q1 + q2
    
class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        tree = Tree([0]*len(nums))
        rank = {v: i for i, v in enumerate(sorted(nums))}
        for i in range(len(nums)-1, -1, -1):
            if rank[nums[i]] == 0:
                ans.append(0)
                tree.update(0, 1)
            else:
                ans.append(tree.query(0, rank[nums[i]]-1))
                tree.update(rank[nums[i]], 1)
        return ans[::-1]
