#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int score(set<string> ing, vector<vector<string>> client_like, vector<vector<string>> client_dislike) {
    int ans = 0;
    for (int i = 0; i < client_like.size(); i++) {
        bool b = true;
        for (auto& s : client_dislike[i]) {
            if (ing.find(s) != ing.end()) {
                b = false;
                break;
            }
        }
        if(!b) { continue; }
        for (auto& s : client_like[i]) {
            if (ing.find(s) == ing.end()) {
                b = false;
                break;
            }
        }
        if(b) { ans++; }
    }
    return ans;
}

int main() {
    vector<vector<string> > client_like, client_dislike;
    map<string, vector<int> > ing_likes, ing_dislikes;

    int N;
    cin >> N;
    for(int i = 0; i < N; i++) {
        int n = 0;
        cin >> n;
        client_like.push_back(vector<string>());
        for(int j = 0; j < n; j++) {
            string s;
            cin >> s;
            client_like[i].push_back(s);
            if(ing_likes.find(s) == ing_likes.end()) {
                ing_likes[s] = vector<int>();
            }
            ing_likes[s].push_back(i);
        }
        cin >> n;
        client_dislike.push_back(vector<string>());
        for(int j = 0; j < n; j++) {
            string s;
            cin >> s;
            client_dislike[i].push_back(s);
            if(ing_likes.find(s) == ing_likes.end()) {
                ing_dislikes[s] = vector<int>();
            }
            ing_dislikes[s].push_back(i);
        }
    }

    set<string> ing;
    for (auto& it : ing_likes) {
        if (ing_dislikes.find(it.first) == ing_dislikes.end() || it.second.size() > ing_dislikes[it.first].size()) {
            ing.insert(it.first);
        }
    }
    int sc = score(ing, client_like, client_dislike);
    cerr << sc << endl;
    bool b = true;
    while(b) {
        b = false;
        for(auto& e : ing_likes) {
            string s = e.first;
            if(ing.find(s) == ing.end()) {
                auto p = ing.insert(s);
                int sc_new = score(ing, client_like, client_dislike);
                if (sc_new <= sc) ing.erase(p.first);
                else {
                    b = true;
                    sc = sc_new;
                }
            }
        }
        for(auto& e : ing_dislikes) {
            string s = e.first;
            auto it = ing.find(s);
            if(it != ing.end()) {
                ing.erase(it);
                int sc_new = score(ing, client_like, client_dislike);
                if (sc_new <= sc) ing.insert(s);
                else {
                    b = true;
                    sc = sc_new;
                }
            }
        cerr << sc << endl;
        }
    }
    cout << ing.size() << " ";
    for (auto it = ing.begin(); it != ing.end(); it++) {
        cout << *it << " ";
    }
}