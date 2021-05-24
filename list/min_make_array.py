# https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/

import numpy as np

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        tot = sum(bin(n).count("1") for n in nums)
        return tot + max(np.int64(np.log2(np.array(nums))))
