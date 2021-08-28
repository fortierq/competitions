class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        max_e = 0  # max of an alternating sum of an even number of elements 
        max_o = 0  # max of an alternating sum of an odd number of elements 
        for n in nums:
            max_e, max_o = max(max_e, max_o-n), max(max_o, max_e+n)
        return max(max_e, max_o)
