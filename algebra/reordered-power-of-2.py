import numpy as np


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        def sorted_digits(n):
            return sorted(map(int, list(str(n))))
        d = sorted_digits(N)
        p = len(d)
        l = np.log2(10)
        for k in range(int((p-1)*l), int(p*l) + 1):
            if d == sorted_digits(1 << k):
                return True
        return False
