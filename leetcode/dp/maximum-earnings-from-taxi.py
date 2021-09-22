from collections import defaultdict

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        d = defaultdict(list)
        for r in rides:
            d[r[1]].append(r)
        dp = [0] * (n + 1)
        for i in range(len(dp)):
            dp[i] = dp[i - 1]
            for r in d[i]:
                dp[i] = max(max(dp[i - 1],dp[i]), r[2] + r[1] - r[0] + dp[r[0]])
        return max(dp)
        
