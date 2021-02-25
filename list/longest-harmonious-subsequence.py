#  https://leetcode.com/problems/longest-harmonious-subsequence/

class Solution:
    def findLHS(self, nums) -> int:
        count = {}
        for e in nums:
            if e not in count:
                count[e] = 0
            count[e] += 1
        maxi = 0
        for k in count:
            if k - 1 in count:
                maxi = max(maxi, count[k] + count[k - 1])
        return maxi

s = Solution()
assert s.findLHS([1,3,2,2,5,2,3,7]) == 5
assert s.findLHS([]) == 0
assert s.findLHS([1, 1, 1]) == 0
