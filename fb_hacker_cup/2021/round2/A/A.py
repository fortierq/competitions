from collections import Counter

for i in range(int(input())):
    N, M = list(map(int, input().split()))
    S = Counter(map(int, input().split()))
    T = Counter()
    n = 0
    for _ in range(N):
        P = Counter(map(int, input().split()))
n += sum(T.values()) - sum((T & P).values())
S = S & (P - T & P)
T = P - S
        # print(S)
        # print(T)
    print(f"Case #{i+1}: {n}")
