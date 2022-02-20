from functools import reduce


for _ in range(int(input())):
    input()
    L = map(int, input().split())
    print(reduce(lambda x, y: x | y, L))