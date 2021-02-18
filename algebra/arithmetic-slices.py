class Solution:
    def numberOfArithmeticSlices(self, A) -> int:
        def d(i):
            return A[i + 1] - A[i]

        def n(i, j):
            n = j - i + 1
            return (n - 1) * (n - 2) // 2

        total = 0
        i, j = 0, -1
        for j in range(len(A) - 2):
            if d(j) != d(j + 1):
                total += n(i, j + 1)
                i = j + 1
        return total + n(i, j + 2)
