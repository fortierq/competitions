import heapq

for _ in range(int(input())):
    input()
    L = list(map(int, input().split()))
    q = []
    op = []
    for i in range(1, len(L) - 1):
        for j in range(i + 1, len(L)):
            q.append((L[i] - L[j], i, j))
    q.sort()
    iq = 0
    for i in range(len(L)):
        while iq != len(q) and q[iq][0] < L[i]:
            a, j, k = q[iq]
            iq+=1
            if j > i and (i == 0 or L[i - 1] <= a):
                L[i] = a
                op.append((i, j, k))
        if i != 0 and L[i - 1] > L[i]:
            op = None
            break
    if op is not None:
        print(len(op))
        for i, j, k in op:
            print(i + 1, j + 1, k + 1)
    else:
        print(-1)