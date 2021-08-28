class Solution:
    def hammingWeight(self, n: int) -> int:
        s = 0
        while n != 0:
            s += n % 2
            n >>= 1
        return s

S = Solution()
print(S.hammingWeight(5))