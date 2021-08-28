from functools import cache

class Solution:
    def countSubstrings(self, s):
        @cache
        def dp(i, j):
            if i>=j: return 1
            return dp(i+1, j-1) if s[i]==s[j] else 0
        
        ans = 0
        for i in range(len(s)):
            for j in range(i+1):
                ans += dp(j, i)
        return ans
