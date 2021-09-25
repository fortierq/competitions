from collections import Counter

for i in range(int(input())):
    N, M = list(map(int, input().split()))
    S = Counter(map(int, input().split()))
    T = Counter()
    n = 0
    for _ in range(N):
        P = Counter(map(int, input().split()))
        I = S & P
        n += len(T) - len(T & (P - I))
        T = P - I
        S = I
    print(f"Case #{i+1}: {n}")
