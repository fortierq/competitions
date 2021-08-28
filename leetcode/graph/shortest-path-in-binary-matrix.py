from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        if grid[0][0] == 1:
            return -1
        file = deque([((0, 0), 1)])
        n = len(grid)
        while file:
            next, d = file.popleft()
            if next == (n - 1, n - 1):
                return d
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    p = (next[0] + i, next[1] + j)
                    if 0 <= p[0] < n and 0 <= p[1] < n and grid[p[0]][p[1]] == 0:
                        file.append((p, d + 1))
                        grid[p[0]][p[1]] = 1
        return -1


s = Solution()
print(s.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
print(
    s.shortestPathBinaryMatrix([[0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 1, 0, 0],
                                [0, 0, 0, 1, 1, 1, 0], [1, 0, 0, 1, 1, 0, 0], [1, 1, 1, 1, 1, 0, 1],
                                [0, 0, 1, 0, 0, 0, 0]]))
