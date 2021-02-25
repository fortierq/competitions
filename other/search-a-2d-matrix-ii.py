# see http://twistedoakstudios.com/blog/Post5365_searching-a-sorted-matrix-faster

class Solution:
    def searchMatrix(self, m: List[List[int]], t: int) -> bool:
        i, j = 0, len(m[0]) - 1
        while j >= 0 and i < len(m):
            if m[i][j] > t:
                j -= 1
            elif m[i][j] < t:
                i += 1
            else:
                return True
        return False
