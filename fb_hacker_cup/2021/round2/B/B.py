from collections import defaultdict
import sys
 
# the setrecursionlimit function is
# used to modify the default recursion
# limit set by python. Using this,
# we can increase the recursion limit
# to satisfy our needs
 
sys.setrecursionlimit(10**6)

for i in range(int(input())):
    N = int(input())
    G = defaultdict(list)
    for j in range(N - 1):
        A, B = list(map(int, input().split()))
        G[A].append(B)
        G[B].append(A)

    F = [-1] + list(map(int, input().split()))

    def dfs(r):
        freq = set()
        vus = set()
        def aux(u):
            if u not in vus: 
                vus.add(u)
                freq.add(F[u])
                for v in G[u]:
                    aux(v)
        aux(r)
        return freq

    n = 0
    for u in G:
        for v in G[u]:
            G[u].remove(v)
            G[v].remove(u)
            if len(dfs(u) & dfs(v)) == 0:
                n += 1
            else:
                G[u].append(v)
                G[v].append(u)
    print("Case #{}: {}".format(i + 1, n))
