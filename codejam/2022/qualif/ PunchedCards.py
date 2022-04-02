for i in range(int(input())):
    print(f"Case #{i}:")
    n, k = map(int, input().split())
    print("..+" + "-+"*(k - 1))
    print("..|" + ".|"*(k - 1))
    for _ in range(n - 1):
        print("+" + "-+"*(k))
        print("|" + ".|"*(k))
    print("+" + "-+"*(k))
