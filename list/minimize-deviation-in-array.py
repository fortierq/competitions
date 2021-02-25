class Solution:
    def minimumDeviation(self, nums) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = nums[i] // 2

        nums.sort()
        for i in range(len(nums)):
            dev = max(nums[-1], nums[i - 1]) - min(nums[0], nums[i])
            if i == len(nums) - 1 or 2 * nums[i] - min(nums[0], nums[i + 1]) >= dev:
                print(nums)
                return dev
            nums[i] *= 2

S = Solution()
print(S.minimumDeviation([4,1,5,20,3]))