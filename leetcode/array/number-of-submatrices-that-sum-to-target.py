import numpy as np

def subarraySum(nums, k: int) -> int:
    d = Counter()
    d[0] = 1
    res, cum_sum = 0, 0
    for n in nums:
        cum_sum += n
        res += d[cum_sum - k]
        d[cum_sum] += 1
    return res

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        M = np.array(matrix).cumsum(axis=1)
        res = 0
        for j in range(len(M[0])):
            for i in range(j + 1):
                a = M[:, j] - (M[:, i - 1] if i > 0 else 0)
                res += subarraySum(a, target)
        return res
