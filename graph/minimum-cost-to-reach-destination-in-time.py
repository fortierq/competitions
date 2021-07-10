import numpy as np

class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        M = [[] for i in range(n)]
        for e in edges:
            M[e[0]].append((e[1], e[2]))
            M[e[1]].append((e[0], e[2]))
        dp = np.full((maxTime + 1, n), float('inf'))  # dp[t, v] is the minimum cost of a path from 0 to v with time <= t
        dp[0, 0] = passingFees[0]
        reach = False
        for t in range(1, maxTime + 1):
            for u in range(n):
                for v, time in M[u]:
                    if time <= t:
                        dp[t, u] = min(dp[t, u], dp[t - time, v] + passingFees[u])
        r = min(dp[:, n-1])
        return -1 if r == float('inf') else int(r)
