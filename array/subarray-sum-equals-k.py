from collections import Counter

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = Counter()
        res = 0
        cum_sum = 0
        d[0] = 1
        for n in nums:
            cum_sum += n
            a = cum_sum - k
            if a in d:
                res += d[a]
            d[cum_sum] += 1
        return res
