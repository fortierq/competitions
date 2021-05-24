import numpy as np
from collections import Counter

class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        d = Counter(str(N))
        p = sum(d.values())
        l = np.log2(10)
        return any(
            d == Counter(str(1 << k))
            for k in range(int((p - 1) * l), int(p * l) + 1)
        )
