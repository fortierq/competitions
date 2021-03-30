class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        L = []
        for i, e in enumerate(envelopes):
            m = 1
            for j in range(i):
                m_ = L[j]
                if e[0] >= envelopes[j][0] and e[1] >= envelopes[j][1]:
                    m_ += 1
                m = max(m, m_)
            L.append(m)
        return max(L)
