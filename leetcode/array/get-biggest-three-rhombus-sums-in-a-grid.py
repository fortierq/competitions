from heapq import *


class Solution:
    def getBiggestThree(self, g: List[List[int]]) -> List[int]:
        n, p = len(g), len(g[0])
        
        d_down, d_up = [[0]*p for i in range(n)], [[0]*p for i in range(n)]
        for i in range(n):
            d_down[i][0] = g[i][0]
            d_up[i][0] = g[i][0]
        for j in range(1, p):
            d_down[0][j] = g[0][j]
            for i in range(1, n):
                d_down[i][j] = d_down[i-1][j-1] + g[i][j]
            for i in range(n-1):
                d_up[i][j] = d_up[i+1][j-1] + g[i][j]
            d_up[-1][j] = g[-1][j]
        def val(i, j):
            return 0 <= i < n and 0 <= j < p
        
        q = []
        for i in range(n):
            for j in range(p):
                k = 0
                while val(i + k, j + k) and val(i - k, j + k) and val(i, j+2*k):
                    if k == 0:
                        s = g[i][j]
                    else:
                        s = d_down[i + k][j + k] - d_down[i][j] + d_down[i][j + 2*k] - d_down[i - k][j + k] + d_up[i - k][j + k] - d_up[i][j] - d_up[i + k][j + k] + d_up[i][j + 2*k] + g[i][j] - g[i][j + 2*k] #+ g[i + k][j + k] + g[i - k][j + k]
                    if len(q) < 3 and s not in q:
                        heappush(q, s)
                    elif len(q) > 0 and s > q[0] and s not in q:
                        heappushpop(q, s)
                    k +=1
        return sorted(q)[::-1]
