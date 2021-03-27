from functools import cache

class Solution:
    def countSubstrings(self, s: str) -> int:
        @cache
        def f(i, j):
            if i > j:
                return 0
            res = f(i, j - 1) + f(i + 1, j) - f(i + 1, j - 1)
            if s[i] == s[j]:
                res += f(i + 1, j - 1) + 1
            return res
        return f(0, len(s) - 1)
