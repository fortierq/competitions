for _ in range(int(input())):
    input()
    L = list(map(int, input().split()))
    n = 0
    for i in range(1, len(L) - 1):
        if L[i] > max(L[i + 1], L[i - 1]):
            n += 1
            L[i + 1] = L[i]
            if i + 2 < len(L) and L[i + 2] > L[i+1]:
                L[i + 1] = L[i + 2]
    print(n)
    print(' '.join(map(str,L)))