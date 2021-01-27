import math

def digits(n):
    return int(math.log2(n)) + 1

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        p = 10**9 + 7
        total = 0
        for i in range(1, n+1):
            total <<= digits(i)
            total += i
            total %= p
        return total
            
S = Solution()
print(S.concatenatedBinary(505379714))