from collections import defaultdict

T = int(input())

for i in range(T):
    N = int(input())
    c = list(map(int, input().split(' ')))
    g = defaultdict(list)
    for _ in range(N - 1):
        edge = list(map(int, input().split(' ')))
        g[edge[0]].append(edge[1])
        g[edge[1]].append(edge[0])

    def dfs(u, pere):
        maxi = 0
        for v in g[u]:
            if v != pere:
                maxi = max(maxi, dfs(v, u))
        return maxi + c[u - 1]
    
    L = []
    for v in g[1]:
        L.append(dfs(v, 1))
    L.sort()
    res = c[0]
    if len(L) > 0:
        res += L[-1]
    if len(L) > 1:
        res += L[-2]
    
    print(f"Case #{i + 1}: {res}")
