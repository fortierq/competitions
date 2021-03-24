class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        for b in B:
            j, v = -1, float("inf")
            for i, a in enumerate(A):
                if a == -1:
                    continue
                if b < a < v:
                    j, v = i, a
            if j == -1:
                
            res.append(A[j])
            A[j] = -1
        return res
