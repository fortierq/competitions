# https://leetcode.com/contest/biweekly-contest-33/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        dominant = [True]*n
        for i in range(len(edges)):
            dominant[edges[i][1]] = False
        L = []
        for i in range(n):
            if dominant[i]:
                L.append(i)
        return L
