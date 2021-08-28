class Solution:
    def sumOfFlooredPairs(self, n: List[int]) -> int:
        n.sort()
        c = [0]*(n[-1]+1)
        for e in n:
            c[e] += 1
        for i in range(1, len(c)):
            c[i] += c[i-1]
        res = 0
        for e in n:
            m = 1
            while m*e - 1 < len(c):
                up = c[(m+1)*e - 1] if (m+1)*e - 1 < len(c) else c[-1]
                res += m*(up - c[m*e - 1])
                m += 1
        return res % (10**9 + 7)
