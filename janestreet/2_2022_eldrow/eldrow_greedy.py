from pathlib import Path
import random

words = set()
with open(Path(__file__).parent / 'eldrow.txt') as f:
    for line in f:
        words.add(line.strip())

def guess(w, t):
    L = [0]*5
    for i, c in enumerate(w):
        if c in t:
            if t[i] == c:
                L[i] = 2
            else:
                L[i] = 1
    return L

def satisfy(words, w, g):
    s = set()
    for w_ in words:
        b = True
        for i in range(len(g)):
            if g[i] == 2 and w_[i] != w[i]:
                b = False
                break
            if g[i] == 1 and (w_[i] == w[i] or w[i] not in w_):
                b = False
                break
            if g[i] == 0 and w[i] in w_:
                b = False
                break
        if b:
            s.add(w_)
    return s

s_max, t_max, w_max = set(), None, None
L = list(words)
for _ in range(10):
    w = random.choice(L)
    t = random.choice(L)
    g = guess(w, t)
    s = satisfy(words, w, g)
    if len(s) > len(s_max):
        s_max, t_max, w_max = s, t, w
        print(w_max, t_max, len(s))
# for w in words:
#     for t in words:
#         g = guess(w, t)
#         s = satisfy(words, w, g)
#         if len(s) > len(s_max):
#             print(w_max, t_max, len(s))
#             s_max, t_max, w_max = s, t, w
#             if len(s) > 1300: break

print(w_max)
words, t, w = s_max, t_max, w_max
while len(words) > 1:
    s_max = set()
    for w in words:
            g = guess(w, t)
            s = satisfy(words, w, g)
            if len(s) > len(s_max):
                s_max = s
                w_max = w
    words = s_max
    print(w_max)