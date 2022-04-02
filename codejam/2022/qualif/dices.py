for i in range(int(input())):
    input()
    dices = list(map(int, input().split()))
    dices.sort()
    
    k = 0
    for d in dices:
        if d > k:
            k += 1
    print(f"Case #{i + 1}: {k}")
    