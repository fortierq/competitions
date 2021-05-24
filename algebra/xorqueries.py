class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        acc = list(accumulate(arr, func=lambda x, y: x^y, initial=0))
        return [acc[j + 1]^acc[i] for i, j in queries]
