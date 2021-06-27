#include <algorithm>

class Solution {
public:
    int candy(vector<int>& ratings) {
        vector<int> candies(ratings.size(), 1);
        candies[0] = 1;
        for(int i = 1; i < ratings.size(); i++) {
            if(ratings[i - 1] < ratings[i]) {
                candies[i] = candies[i - 1] + 1;
            }
        }
        for(int i = ratings.size() - 1; i > 0; i--) {
            if(ratings[i - 1] > ratings[i]) {
                candies[i - 1] = std::max(candies[i - 1], candies[i] + 1);
            }
        }
        
        int s = 0;
        for (const auto& n : candies)
            s += n;
        return s;
    }
};
