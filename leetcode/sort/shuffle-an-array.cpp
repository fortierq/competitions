#include <stdlib.h> 

class Solution {
public:
    vector<int>& nums;
    Solution(vector<int>& nums): nums(nums) {
        
    }
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        return nums;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        vector<int> res = nums;
        for(int i = 1; i < res.size(); i++) {
            int tmp = res[i];
            int j = std::rand() % (i+1);
            res[i] = res[j];
            res[j] = tmp;
        }
        return res;
    }
};
