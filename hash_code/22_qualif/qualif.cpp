#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;
map<string, map<string, int>> contributors;
map<string, vector<pair<string, int>>> project_skills;
map<string, int> project_days;
map<string, int> project_score;
map<string, int> project_deadline;
vector<string> projects;

bool cmp(string s1, string s2) {
    return project_days[s1] < project_days[s2];
}

bool mentor(vector<string> &assigned, string skill, int lvl) {
    for (auto& s : assigned) {
        if (contributors[s][skill] >= lvl) {
            return true;
        }
    }
    return false;
}

vector<string> is_possible(string project) {
    vector<string> assigned;
    for (auto& p : project_skills[project]) {
        bool b = false;
        for (auto& c : contributors) {
            if (c.second[p.first] >= p.second && find(assigned.begin(), assigned.end(), c.first) == assigned.end()) {
                assigned.push_back(c.first);
                b = true;
                break;
            }
        }
        if (!b && mentor(assigned, p.first, p.second)) {
            for (auto& c : contributors) {
                if (c.second[p.first] == p.second - 1 && find(assigned.begin(), assigned.end(), c.first) == assigned.end()) {
                    assigned.push_back(c.first);
                    break;
                }
            }
        }
    }
    return assigned;
}

int main() {
    int n_contributors, n_projects;
    cin >> n_contributors >> n_projects;
    
    for (int i = 0; i < n_contributors; i++) {
        string name;
        cin >> name;
        contributors[name] = map<string, int>();
        int n;
        cin >> n;
        for (int j = 0; j < n; j++) {
            string project;
            cin >> project;
            int lvl;
            cin >> lvl;
            contributors[name][project] = lvl;
        }
    }
    for (int i = 0; i < n_projects; i++) {
        string project;
        cin >> project;
        projects.push_back(project);
        int n1, n2, n3, n4;
        cin >> n1 >> n2 >> n3 >> n4;
        project_days[project] = n1;
        project_score[project] = n2;
        project_deadline[project] = n3;
        project_skills[project] = vector<pair<string, int>>();
        for (int j = 0; j < n4; j++) {
            string skill;
            cin >> skill;
            cin >> n1;
            project_skills[project].push_back(pair<string, int>(skill, n1));
        }
    }

    sort(projects.begin(), projects.end(), cmp);

    vector<string> selected_projects;
    map<string, vector<string>> assigned_projects;
    for (auto& p : projects) {
        auto assigned = is_possible(p);
        if (assigned.size() == project_skills[p].size()) {
            selected_projects.push_back(p);
            assigned_projects[p] = assigned;
            for(int i = 0; i < assigned.size(); i++) {
                if(project_skills[p][i].second >= contributors[assigned_projects[p][i]][project_skills[p][i].first]) {
                    contributors[assigned_projects[p][i]][project_skills[p][i].first]++;
                }
            }
        }
    }

    cout<<selected_projects.size()<<endl;
    for (auto& p : selected_projects) {
        cout<<p<<endl;
        for (auto& c : assigned_projects[p]) {
            cout<<c<<" ";
        }
        cout<<endl;
    }
}