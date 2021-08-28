class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        d = dict()
        for r in arr:
            n = 1
            for k in d:
                if r / k in d:
                    n += d[r / k] * d[k]
            d[r] = n
        return sum(d.values()) % (10**9 + 7)
