for i in range(int(input())):
    m = [float("inf")]*4
    for _ in range(3):
        L = list(map(int, input().split()))
        for j in range(4):
            m[j] = min(m[j], L[j])
    print(f"Case #{i + 1}:", end=" ")
    if sum(m) < 1e6:
        print("IMPOSSIBLE")
    else:
        s = 1e6
        for i in range(4):
            print(int(min(s, m[i])), end=" ")
            s -= min(s, m[i])
        print()
    