from collections import Counter

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        d = Counter(nums)
        res = 0
        while len(d) > 0:
            d_ = Counter()
            for k in d:
                if k == target:
                    res += d[k]
                elif k < target:
                    for n in nums:
                        d_[k + n] += d[k]
            d = d_
        return res
