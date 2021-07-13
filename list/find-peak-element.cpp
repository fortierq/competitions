class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int i = 0, j = nums.size();
        while (true) {
            int m = (i + j)/2;
            if(m > 0 && nums[m-1] > nums[m])
                j = m;
            else if(m < nums.size() - 1 && nums[m+1] > nums[m])
                i = m + 1;
            else
                return m;
        }
    }
};
