class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        if(wall.empty())
            return 0;
        unsigned int length = 0;
        for(auto &v: wall[0])
            length += v;
        vector<unsigned int> count(length + 1, 0);
        for(const auto &r: wall) {
            unsigned int sz = 0;
            for(int i=0; i < r.size() - 1; ++i) {
                sz += r[i];
                count[sz]++;
            }
        }
        unsigned int maxi = 0;
        for (auto &n: count)
            if (n > maxi)
                maxi = n;
        return wall.size() - maxi;
    }
};
