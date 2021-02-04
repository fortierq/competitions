#  https://leetcode.com/problems/longest-harmonious-subsequence/

class Solution:
    def findLHS(self, nums) -> int:
        lhs_maxi = {}  # lhs_maxi[v] is the LHS whose maximum is v
        for e in nums:
            for m in [e - 1, e]:
                if m not in lhs_maxi:
                    lhs_maxi[m] = 0
                lhs_maxi[m] += 1
        val = lhs_maxi.values()
        if len(val) == 0:
            return 0
        return max(val)

s = Solution()
assert s.findLHS([1,3,2,2,5,2,3,7]) == 5
assert s.findLHS([]) == 0
