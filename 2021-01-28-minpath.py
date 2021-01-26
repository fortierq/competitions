from heapq import heappush, heappop

class Solution:
    def minimumEffortPath(self, h) -> int:
        n, p = len(h), len(h[0])
        efforts = [[None for _ in range(p)] for _ in range(n)]
        F = []
            
        def edge(u, v):
            return (abs(h[u[0]][u[1]] - h[v[0]][v[1]]), v, u)
        
        def add(u, v):
            heappush(F, edge(u, v))
        
        if n > 1: add((0, 0), (1, 0))
        if p > 1: add((0, 0), (0, 1))
        efforts[0][0] = 0

        while F != []:
            w, v, u = heappop(F)
            if efforts[v[0]][v[1]] is None:
                efforts[v[0]][v[1]] = max(efforts[u[0]][u[1]], w)
                if v == (n-1, p-1):
                    return efforts[v[0]][v[1]]
                for i in [-1, 1]:
                    if 0 <= v[0] + i < n:
                        add(v, (v[0] + i, v[1]))
                    if 0 <= v[1] + i < p:
                        add(v, (v[0], v[1] + i))
        return 0

S = Solution()
h = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
print(S.minimumEffortPath(h))
print(S.minimumEffortPath([[3]]))