from collections import deque

class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        order = list(range(len(B)))
        ans = [0]*len(A)
        order.sort(key=lambda x: -B[x])
        A = deque(sorted(A))
        for ix in order:
            ans[ix] = A.pop() if A[-1] > B[ix] else A.popleft()
        return ans
