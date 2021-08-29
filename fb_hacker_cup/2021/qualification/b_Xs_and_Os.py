import numpy as np

def sol(M):
    mini = float("inf")
    n_mini = 0
    singles = set()

    def update(T, pos):
        nonlocal mini, n_mini
        unique, count = np.unique(T, return_counts=True)

        if "O" not in unique:
            if "." not in unique:
                n_dot = 0
            else:
                n_dot = count[np.where(unique == ".")[0][0]]
            if n_dot < mini:
                n_mini = 0
                mini = n_dot
            if mini == n_dot:
                if mini == 1:
                    i = np.where(T == ".")[0][0]
                    p = (i, pos[0]) if pos[1] == 1 else (pos[0], i)
                    if p in singles:
                        return
                    singles.add(p)
                n_mini += 1

    for i in range(len(M)):
        update(M[i], (i, 0))
    
    for j in range(len(M)):
        update(M[:, j], (j, 1))

    return mini, n_mini

T = int(input())

for i in range(T):
    N = int(input())
    M = []
    for _ in range(N):
        row = []
        for c in input():
            row.append(c)
        M.append(row)
    mini, n_mini = sol(np.array(M))
    if mini == float("inf"):
        print(f"Case #{i+1}: Impossible")
    else:
        print(f"Case #{i+1}: {mini} {n_mini}")
    