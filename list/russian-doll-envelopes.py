
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        G = {v : [] for v in range(n)}
        cur = set(v for v in range(n))
        for i, e in enumerate(envelopes):
            for j, f in enumerate(envelopes):
                if e[0] < f[0] and e[1] < f[1]:
                    G[i].append(j)
                    cur.discard(j)
        d = 0
        next = set()
        while len(cur) != 0:
            u = cur.pop()
            for v in G[u]:
                next.add(v)
            if len(cur) == 0:
                d += 1
                cur, next = next, set()
        return d
