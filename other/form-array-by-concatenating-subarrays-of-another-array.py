class Solution:
    def canChoose(self, g: List[List[int]], nums: List[int]) -> bool:
        i = 0
        j = 0
        while j < len(nums):
            if i >= len(g):
                return True
            if g[i] == nums[j:j + len(g[i])]:
                j = j + len(g[i]) - 1
                i += 1
            j += 1
        return i >= len(g)
