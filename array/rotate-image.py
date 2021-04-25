import numpy as np


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = np.ones((n, n), int)
        for i in range(n):
            for j in range(n):
                m[j, n - 1 - i] = matrix[i][j]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = m[i, j]
