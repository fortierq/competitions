#  https://leetcode.com/problems/shortest-distance-to-a-character/


class Solution:
    def hat(self, L, i, j):
        for k in range(i, j):
            L[k] = min(k - i, j - k)

    def shortestToChar(self, s: str, c: str):
        ind_c = []
        for i, e in enumerate(s):
            if e == c:
                ind_c.append(i)
        dist = [0] * len(s)
        for i in range(ind_c[0]):
            dist[i] = ind_c[0] - i
        for j in range(0, len(ind_c) - 1):
            self.hat(dist, ind_c[j], ind_c[j + 1])
        for i in range(ind_c[-1], len(dist)):
            dist[i] = i - ind_c[-1]
        return dist
