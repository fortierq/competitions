#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

bool cmp(pair<string, int>& a, pair<string, int>& b)
{
    return a.second < b.second;
}

int main() {
    vector<string> likes, dislikes;
    map<string, int> n_likes, n_dislikes;
    
    int N;
    cin >> N;
    for(int i = 0; i < N; i++) {
        int n = 0;
        cin >> n;
        for(int j = 0; j < n; j++) {
            string s;
            cin >> s;
            likes.push_back(s);
            if(n_likes.find(s) != n_likes.end()) {
                n_likes[s] = 0;
            }
            n_likes[s]++;
        }
        cin >> n;
        for(int j = 0; j < n; j++) {
            string s;
            cin >> s;
            dislikes.push_back(s);
            if(n_likes.find(s) != n_likes.end()) {
                n_likes[s] = 0;
            }
            n_likes[s]--;
        }
    }

    vector<string> A;
  
    for (auto& it : n_likes) {
        if (it.second > 0) {
            A.push_back(it.first);
        }
    }
    cout << A.size() << " ";
    for (auto it = A.begin(); it != A.end(); it++) {
        cout << *it << " ";
    }
    // sort(A.begin(), A.end(), cmp);

    // vector<string> ans;
    // for(auto& it : A) {
    //     if(it.second > 0) {
    //         cout << it.first << endl;
    //     }
    // }
}