class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def nice(i, j):
            for k in range(i, j):
                if s[k].isupper() and s[k].lower() not in s[i:j]:
                    return False
                if s[k].islower() and s[k].upper() not in s[i:j]:
                    return False
            return True
        res = ""
        for j in range(len(s)):
            for i in range(j):
                n = j - i + 1
                if n > len(res) and nice(i, j + 1):
                    res = s[i: j+1]
        return res
