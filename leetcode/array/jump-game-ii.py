class Solution {
public:
    int jump(vector<int>& nums) {
        vector<int> jumps(nums.size(), INT_MAX);
        jumps[0] = 0;
        for(int i = 0; i < nums.size(); i++) 
            for(int j = i+1; j <= i + nums[i] && j < nums.size(); j++) 
                jumps[j] = min(jumps[j], jumps[i] + 1);
        return jumps.back();
    }
};
