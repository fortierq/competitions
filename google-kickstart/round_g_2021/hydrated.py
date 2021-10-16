

for j in range(int(input())):
    objects = []
    for _ in range(int(input())):
        objects.append(list(map(int, input().split(" "))))

    def mini(a, b):
        L = [o[a] for o in objects] + [o[b] for o in objects]
        L.sort()
        return L[max(0, len(L)//2 - 1)]

    print(f"Case #{j + 1}: {mini(0, 2)} {mini(1, 3)}")
