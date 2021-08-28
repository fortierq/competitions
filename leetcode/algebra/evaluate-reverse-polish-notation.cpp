class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        vector<int> pile;
        for (auto &t: tokens) {
            try {
                pile.push_back(stoi(t));
            }
            catch (const std::invalid_argument& ia) {
                int a = pile.back();
                pile.pop_back();
                int b = pile.back();
                pile.pop_back();
                if (t == "+")
                    pile.push_back(a + b);
                if (t == "-")
                    pile.push_back(b - a);
                if (t == "*")
                    pile.push_back(a * b);
                if (t == "/")
                    pile.push_back(int(b / a));
                
            }
        }
        return pile[0];
    }
};
