class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        L = sorted(nums)
        i = 0
        for i in range(len(L)):
            if nums[i] != L[i]:
                break
            if i == len(L) - 1:
                return 0
        j = len(L) - 1
        for j in range(len(L) - 1, -1, -1):
            if nums[j] != L[j]:
                break
        return j - i + 1
