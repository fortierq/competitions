class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds, dt = dict(), dict()
        for u, d in (s, ds), (t, dt):
            for c in u:
                if c not in d:
                    d[c] = -1 
                d[c] += 1
        return ds == dt