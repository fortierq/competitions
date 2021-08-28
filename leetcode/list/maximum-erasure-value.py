class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = 0
        i = 0
        s = set()
        for k in nums:
            if k in s:
                res = max(res, sum(s))
                while nums[i] != k:
                    s.remove(nums[i])
                    i += 1
                i += 1
            s.add(k)
        return max(res, sum(s))
