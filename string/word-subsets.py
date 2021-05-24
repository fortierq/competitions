from collections import Counter

class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        res = []
        s = Counter()
        for b in B:
            b = Counter(b)
            for k in b:
                if b[k] > s[k]:
                    s[k] = b[k]
        for a in A:
            a_ = Counter(a)
            universal = all(a_[k] >= s[k] for k in s)
            if universal:
                res.append(a)
        return res
