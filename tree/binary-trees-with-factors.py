class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        d = {}
        for r in arr:
            n = 1 + sum(d[r / k] * v for k, v in d.items() if r / k in d)
            d[r] = n
        return sum(d.values()) % (10**9 + 7)
