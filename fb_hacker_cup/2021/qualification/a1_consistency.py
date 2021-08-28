vowels = ["A", "E", "I", "O", "U"]
def letters():
    yield from map(chr, range(65, 65+26))

def dp(S):
    d = {l: 0 for l in letters()}
    for c in S:
        for letter in letters():
            if letter == c:
                continue
            if (letter in vowels and c in vowels) or (letter not in vowels and c not in vowels):
                d[letter]  = d[letter] + 2
            else:
                d[letter]  = d[letter] + 1
    return min(d.values())

k = int(input())
for i in range(k):
    print(f"Case #{i+1}: {dp(input())}")
