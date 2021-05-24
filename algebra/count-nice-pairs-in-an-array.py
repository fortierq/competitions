class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        rev = [int(str(n)[::-1]) for n in nums]
        s = {}
        for i in range(len(nums)):
            k = nums[i] - rev[i]
            if k not in s:
                s[k] = 0
            s[k] += 1
        res = sum(s[k] * (v - 1) // 2 for k, v in s.items())
        return res % (10**9 + 7)
