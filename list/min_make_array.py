# https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/

import numpy as np

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        tot = 0 
        for n in nums:
            tot += bin(n).count("1")
        return tot + max(np.int64(np.log2(np.array(nums))))
