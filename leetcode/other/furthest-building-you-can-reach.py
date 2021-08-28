from heapq import *


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        q = []
        h_ = heights[0]
        for i in range(1, len(heights)):
            h = heights[i]
            if h > h_:
                l = h - h_
                if len(q) < ladders:
                    heappush(q, l)
                else:
                    if q and l > q[0]:
                        bricks -= heappushpop(q, l)
                    else:
                        bricks -= l
                    if bricks < 0:
                        return i - 1
            h_ = h
        return i
