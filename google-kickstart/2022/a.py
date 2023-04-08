for k in range(int(input())):
    input()
    A = list(map(int, input().split(" ")))
    s = 0
    for i in range(len(A)):
        p = 0
        for j in range(i, len(A)):
            p += A[j]
            if p < 0:
                break
            s += p
        
    print(f"Case #{k+1}: {s}")
