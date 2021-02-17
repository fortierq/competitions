class Solution:
    def maxArea(self, height) -> int:
        def area(i, j):
            return (j - i) * min(height[i], height[j])

        i, j = 0, len(height) - 1
        m = 0
        while i < j:
            m = max(m, area(i, j))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return m