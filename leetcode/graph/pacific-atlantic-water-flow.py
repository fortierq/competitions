class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        n, m = len(matrix), len(matrix[0])
        moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        def dfs(S):
            vus = set()
            while len(S) != 0:
                s = S.pop()
                if s not in vus:
                    vus.add(s)
                    for i, j in moves:
                        if 0 <= i + s[0] < n and 0 <= j + s[1] < m:
                            if matrix[s[0]][s[1]] <= matrix[i + s[0]][j + s[1]]:
                                S.add((i + s[0], j + s[1]))
            return vus
        S = dfs(set((0, j) for j in range(m)) | set((i, 0) for i in range(n))) & dfs(set((n - 1, j) for j in range(m)) | set((i, m - 1) for i in range(n)))
        return [[s[0], s[1]] for s in S]
