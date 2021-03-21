import numpy as np
from collections import Counter

class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        def sorted_digits(n):
            return sorted(map(int, list(str(n))))
        d = Counter(str(N))
        p = sum(d.values())
        l = np.log2(10)
        for k in range(int((p-1)*l), int(p*l) + 1):
            if d == Counter(str(1 << k)):
                return True
        return False
