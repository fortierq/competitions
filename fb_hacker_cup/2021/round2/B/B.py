for i_ in range(int(input())):
    R, C, K = list(map(int, input().split()))
    G = [["."]*C]
    for j in range((R)):
        G.append(list(input()))
    G.append(["."]*C)

    def f(i_, G, K):
        m = 0
        L = [0]*C
        for j in range(K):
            for k in range(C):
                if G[j][k] == "X":
                    L[k] += 1
        
        for i in range(K, R):
            m_ = -(i - K)
            for j in range(C):
                if G[i][j] == "X":
                    L[j] += 1
                else:
                    if L[j] < K:
                        m_ += 1
            m = max(m, m_)
        return C - m
    
    print("Case #{}: {}".format(i_+1, min(f(i_, G, K), f(i_, G[::-1], R + 1 - K))))
