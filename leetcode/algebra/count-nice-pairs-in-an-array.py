class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        rev = [int(str(n)[::-1]) for n in nums]
        s = dict()
        for i in range(len(nums)):
            k = nums[i] - rev[i]
            if k not in s:
                s[k] = 0
            s[k] += 1
        res = 0
        for k in s:
            res += s[k]*(s[k] - 1)//2
        return res % (10**9 + 7)
