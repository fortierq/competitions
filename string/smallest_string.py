# https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

class Solution:
    def letter(self, p):
        return chr(ord('a') + p - 1)

    def getSmallestString(self, n: int, k: int) -> str:
        L = []
        r = k
        for i in range(n):
            m = min(26, r - (n - i - 1))
            c = self.letter(m)
            L.append(c)
            r -= m
        return ''.join(L[::-1])

S = Solution()
print(S.getSmallestString(5, 6))