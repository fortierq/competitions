# https://leetcode.com/problems/non-overlapping-intervals/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda I: I[1])
        remain = [True for i in range(len(intervals))]
        removed = 0
        deb = [(intervals[i], i) for i in range(len(intervals))]
        deb.sort(key = lambda I: I[0][0])
        j = 0
        for i in range(len(intervals)):
            if remain[i]:
                while j < len(intervals) and deb[j][0][0] < intervals[i][1]:
                    if deb[j][1] != i:
                        removed += 1
                        remain[deb[j][1]] = False
                    j += 1
        return removed