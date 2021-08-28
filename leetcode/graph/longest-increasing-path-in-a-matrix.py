from functools import cache

class Solution:
    def longestIncreasingPath(self, M):
        @cache
        def dfs(i, j, v):
            if 0 <= i < n and 0 <= j < p and M[i][j] < v:
                return 1 + max(dfs(k, l, M[i][j]) for k, l in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)])
            return 0

        if len(M) == 0: return 0
        n, p = len(M), len(M[0])
        return max(dfs(x, y, float("inf")) for x in range(n) for y in range(p))
