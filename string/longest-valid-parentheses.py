class Solution:
    def longestValidParentheses(self, s: str) -> int:
        last = 0
        n = 0
        res = 0
        for i, c in enumerate(s):
            if c == "(": 
                n += 1
            else:
                n -= 1
                if n < 0:
                    last = i + 1
                    n = 0
            if n == 0:
                res = max(res, i - last + 1)
        res = max(res, len(s) - last - n)
        return res
