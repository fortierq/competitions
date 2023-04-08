for k in range(int(input())):
    N, E = map(int, input().split(" "))
    X, Y, C = [], [], []
    nectar = dict()
    for i in range(N):
        x, y, c = map(int, input().split(" "))
        X.append(x)
        Y.append(y)
        C.append(c)
        nectar[(x, y)] = c

    vu = dict()
    def dfs(x, y, right):
        k = (x, y, right)
        if k not in vu: 
            vu[k] = 0
            e = nectar.get((x, y), 0)
            for x_ in range(x+1, )
            vu[k] = max(dfs(x + right, y, right), dfs(x - right, y, - right) - E) + e
        return vu[k]

    dfs(0, 10**18, 1)
    print(f"Case #{k+1}: {X}")
