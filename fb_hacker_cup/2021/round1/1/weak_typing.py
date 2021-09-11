for i in range(int(input())):
    a = int(input())
    last = "F"
    res = 0
    for c in input():
        if set([c, last]) == set(["X", "O"]):
            res += 1
        if c != "F":
            last = c
    print(f"Case #{i+1}: {res}")
