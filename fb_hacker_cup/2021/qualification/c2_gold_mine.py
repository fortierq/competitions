from collections import defaultdict

T = int(input())

def pair(L):
    if len(L) % 2 == 1:
        return [L[0]] + pair(L[1:])
    return [L[i] + L[i + 1] for i in range(0, len(L), 2)]

for i in range(T):
    N, K = map(int, input().split(' '))
    c = list(map(int, input().split(' ')))
    g = defaultdict(list)
    inter_paths = []

    for _ in range(N - 1):
        edge = list(map(int, input().split(' ')))
        g[edge[0]].append(edge[1])
        g[edge[1]].append(edge[0])

    def dfs(u, pere):
        L = []
        for v in g[u]:
            if v != pere:
                L.append(dfs(v, u))
        L.sort()
        if len(L) == 0:
            return c[u - 1]
        maxi = L.pop()
        inter_paths.extend(pair(L))
        return maxi + c[u - 1]
    
    L = []
    for v in g[1]:
        L.append(dfs(v, 1))
    L.sort()
    res = c[0]
    if K > 0:
        if len(L) > 0:
            res += L.pop()
        if len(L) > 0:
            res += L.pop()
        
        inter_paths.extend(pair(L))
        inter_paths.sort()
        if K > 1:
            res += sum(inter_paths[-(K-1):])

    print(f"Case #{i + 1}: {res}")
