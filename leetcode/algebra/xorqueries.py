class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        acc = list(accumulate(arr, func=lambda x, y: x^y, initial=0))
        res = []
        for i, j in queries:
            res.append(acc[j + 1]^acc[i])
        return res
