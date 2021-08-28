class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int maxi = 0;
        int cur_start = 0;
        int nzeros = 0;
        for(int i = 0; i < nums.size(); ++i) {
            if(nums[i] == 0) {
                nzeros++;
                if(nzeros > k) {
                    while(nums[cur_start] == 1)
                        cur_start++;
                    cur_start++;
                }
            }
            maxi = std::max(maxi, i - cur_start + 1);
        }
        return maxi;
    }
};
