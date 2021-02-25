// https://leetcode.com/problems/reorder-list/

class Solution {
public:
    void reorderList(ListNode* head) {
        std::vector<ListNode*> v;
        ListNode* cur = head;
        while (cur != nullptr) {
            v.push_back(cur);
            cur = cur->next;
        }
        for (int i = 0; i < v.size() / 2; i++) {
            int j = v.size() - i - 1; // i mirror
            v[i]->next = v[j];
            v[j]->next = v[i + 1];
        }
        if (v.size() > 0) 
            v[v.size() / 2]->next = nullptr; // last element
    }
};