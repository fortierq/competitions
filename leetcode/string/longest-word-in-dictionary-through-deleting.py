class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        n = len(d)
        ind = [0] * n
        res = ""
        for c in s:
            for i in range(n):
                if ind[i] < len(d[i]) and d[i][ind[i]] == c:
                    ind[i] += 1
                if ind[i] == len(d[i]) and (len(d[i]) > len(res) or (len(d[i]) == len(res) and d[i] < res)):
                    res = d[i]
        return res
