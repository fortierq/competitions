# https://leetcode.com/contest/biweekly-contest-33/problems/detect-cycles-in-2d-grid/

class Solution:
    def dfs(self, i, j, pi, pj, grid, vus):
        n, m = len(grid), len(grid[0])
        if vus[i][j] == 1:
            return True
        vus[i][j] = 1
        L = [(i - 1, j), (i, j - 1), (i + 1, j), (i, j +1)]
        return any(
            0 <= a < n
            and 0 <= b < m
            and (a != pi or b != pj)
            and grid[i][j] == grid[a][b]
            and self.dfs(a, b, i, j, grid, vus)
            for (a, b) in L
        )
        
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        vus = [[0]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if vus[i][j] != 1 and self.dfs(i, j, i, j, grid, vus):
                    return True
        return False