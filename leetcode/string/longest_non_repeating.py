# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        d = {}
        i = 0
        for j in range(len(s)):
            if s[j] not in d:
                d[s[j]] = 1
                res = max(res, j - i + 1)
            else:
                while s[i] != s[j]:
                    del d[s[i]]
                    i += 1
                i += 1
        return res
                    