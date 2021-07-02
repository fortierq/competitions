#include <algorithm> 
#include <stdlib.h> 

class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        vector<pair <int,int> > dist;
        vector<int> res;
        for(int e : arr)
            dist.push_back(make_pair(-abs(e - x), -e));
        make_heap(dist.begin(), dist.end());
        for(int i=0; i < k; ++i) {
            pop_heap(dist.begin(), dist.end());
            res.push_back(-dist.back().second);
            dist.pop_back();
        }
        sort(res.begin(), res.end());
        return res;
    }
};
