from heapq import *
from typing import List


class Solution:
    
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        q = []
        tot = 0
        for c in courses:
            if tot + c[0] <= c[1]:
                heappush(q, -c[0])
                tot += c[0]
            elif q and -q[0] > c[0]:
                tot += heapreplace(q, -c[0]) + c[0]
        return len(q)

S = Solution()
print(S.scheduleCourse([[5,5],[4,6],[2,6]]))