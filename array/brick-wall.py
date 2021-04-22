#include <map>

class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        if(wall.empty())
            return 0;
        map<unsigned int, unsigned int> m;
        for(const auto &r: wall) {
            unsigned int sz = 0;
            for(int i=0; i < r.size() - 1; ++i) {
                sz += r[i];
                m[sz]++;
            }
        }
        unsigned int maxi = 0;
        for (auto &p: m)
            if (p.second > maxi)
                maxi = p.second;
        return wall.size() - maxi;
    }
};
