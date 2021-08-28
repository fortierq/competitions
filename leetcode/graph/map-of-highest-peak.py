from collections import deque


class Solution:
    def highestPeak(self, w: List[List[int]]) -> List[List[int]]:
        S = []
        for i in range(len(w)):
            for j in range(len(w[i])):
                if w[i][j] == 1:
                    S.append((i, j, 0))
                w[i][j] = -1

        f = deque(S)
        while f:
            i, j, d = f.popleft()
            if w[i][j] == -1:
                w[i][j] = d
                for (k, l) in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= k < len(w) and 0 <= l < len(w[0]):
                        f.append((k, l, d + 1))
        return w
