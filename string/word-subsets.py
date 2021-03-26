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
            universal = True
            a_ = Counter(a)
            for k in s:
                if a_[k] < s[k]:
                    universal = False
                    break
            if universal:
                res.append(a)
        return res
