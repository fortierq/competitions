class Solution:
    def maxArea(self, height) -> int:
        def area(i, j): 
            return (j - i) * min(height[i], height[j])

        i, j = 0, len(height) - 1
        m = 0
        while i < j:
            m = max(m, area(i, j))
            if height[i] < height[j]:
                ii = i + 1
                while ii < j and height[ii] <= height[i]:
                    ii += 1
                i = ii
            else:
                jj = j - 1
                while jj > i and height[jj] <= height[j]:
                    jj -= 1
                j = jj
        return m