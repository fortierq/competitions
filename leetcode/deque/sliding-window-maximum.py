from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque([])
        ans = []
        for i, n in enumerate(nums):
            while len(q) > 0 and n > q[-1][0]:
                q.pop()
            q.append((n, i))
            while q[0][1] <= i - k:
                q.popleft()
            ans.append(q[0][0])
        return ans[k-1:]