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
best = []
while True:
    w = random.choice(L)
    list_w = [w]
    t = random.choice(L)
    g = guess(w, t)
    s = satisfy(words, w, g)
        
    while len(s) > 1:
        s_max = set()
        for w in s:
            g = guess(w, t)
            s_ = satisfy(s, w, g)
            if len(s_) > len(s_max):
                s_max = s_
                w_max = w
        s, w = s_max, w_max
        list_w.append(w)
    if len(list_w) > max(11, len(best)):
        best = list_w
        print(len(best), ','.join(best))
