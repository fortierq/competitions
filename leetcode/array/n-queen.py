from collections import OrderedDict

def backtrack(n):
    rows, diag_up, diag_down = OrderedDict(), set(), set()
    def f(j):
        if j == n:
            yield list(map(lambda k: '.'*k + 'Q' + '.'*(n - k - 1), rows))
        else:
            for i in range(n):
                if not (i in rows or j + i in diag_up or j - i in diag_down):
                    rows[i] = 0
                    diag_up.add(i + j)
                    diag_down.add(j - i)
                    yield from f(j + 1)
                    rows.pop(i)
                    diag_up.remove(i + j)
                    diag_down.remove(j - i)
    yield from f(0)
    
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        return list(backtrack(n))
