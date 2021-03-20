class Solution:
    def getMaximumConsecutive(self, A):
        res = 1  # number of values we got so far
        for a in sorted(A):
            if a > res: break
            res += a  # we can get values a, a + 1, ..., a + res - 1
        return res
