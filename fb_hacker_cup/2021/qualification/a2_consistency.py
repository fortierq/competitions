from collections import defaultdict
from copy import deepcopy

def letters():
    yield from map(chr, range(65, 65+26))

def dp(S, replacements):
    d = {l: 0 for l in letters()}
    for c in S:
        for letter in letters():
            if letter == c:
                continue
            d[letter] = d[letter] + replacements[c][letter]
    v = min(d.values())
    return -1 if v == float("inf") else v

for i in range(int(input())):
    S = input()
    k = int(input())
    replacements = defaultdict(lambda: defaultdict(lambda: float("inf")))
    for _ in range(k):
        r = input()
        replacements[r[0]][r[1]] = 1

    trans = deepcopy(replacements)
    for _ in range(26):
        for u in letters():
            for v in letters():
                for w in replacements[u]:
                    trans[u][v] = min(trans[u][v], 1 + trans[w][v])


    print(f"Case #{i+1}: {dp(S, trans)}")
