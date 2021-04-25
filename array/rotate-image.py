
class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """            
        n = len(m)
        def rot(i, j):
            return n - 1 - j, i
        
        for i in range((n+1)//2):
            for j in range(n//2):
                k, l = i, j
                tmp = m[i][j]
                for p in range(4):
                    k_, l_ = rot(k, l)
                    m[k][l] = m[k_][l_] if p < 3 else tmp
                    k, l = k_, l_
