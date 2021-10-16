
for j in range(int(input())):
    N, D, C, M = map(int, input().split(" "))
    res = "YES"
    S =input()
    for i, c in enumerate(S):
        if c == "D":
            C += M
            D -= 1
            if D < 0:
                res = "NO"
                break
        else:
            C -= 1
            if C < 0:
                if "D" in S[i+1:]:
                    res = "NO"
                break
    print(f"Case #{j+1}: {res}")
