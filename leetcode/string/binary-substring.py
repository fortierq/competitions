class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev, cur = 0, 0
        res = 0
        for i, c in enumerate(s):
            if i > 0 and s[i] != s[i - 1]:
                res += min(prev, cur)
                prev = cur
                cur = 0
            cur += 1
        return res + min(prev, cur)
