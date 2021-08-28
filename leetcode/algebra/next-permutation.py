class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        i -= 1  # i is the highest index s.t. nums[i] < nums[i + 1]
        if i == -1:  # last permutation
            nums[:] = nums[::-1]
            return
        for j in range(len(nums) - 1, i, -1):
            if nums[j] > nums[i]:
                break
        nums[i], nums[j] = nums[j], nums[i]  # j is the highest index s.t. nums[i] < nums[j]
        nums[i + 1:] = nums[:i:-1]


S = Solution()
p = [0, 1, 2, 5, 3, 3, 0]
S.nextPermutation(p)
print(p)
p = [3, 2, 1]
S.nextPermutation(p)
print(p)