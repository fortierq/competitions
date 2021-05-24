# https://leetcode.com/contest/biweekly-contest-33/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        dominant = [True]*n
        for edge in edges:
            dominant[edge[1]] = False
        return [i for i in range(n) if dominant[i]]
