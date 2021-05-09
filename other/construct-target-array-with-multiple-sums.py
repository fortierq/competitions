from heapq import *

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        q = [-t for t in target]
        heapify(q)  # use max heap
        while True:
            maxi = -heappop(q)
            s = -sum(q)
            if maxi == 1:  # there are only ones
                return True
            if maxi <= s or s == 0:  # this is not possible
                return False
            heappush(q, -(maxi % s))  # remove s from maxi while possible
