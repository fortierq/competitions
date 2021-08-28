#include <string>

class Solution
{
public:
    std::string minRemoveToMakeValid(std::string s)
    {
        std::string s1("");
        int k = 0;
        for (const char &c : s)
        {
            if (c == ')')
            {
                if (k > 0)
                    k--;
                else
                    continue;
            }
            if (c == '(')
                k++;
            s1.push_back(c);
        }
        std::string s2("");
        std::string rev_s1(s1.rbegin(), s1.rend());
        k = 0;
        for (const char &c : rev_s1)
        {
            if (c == '(')
            {
                if (k > 0)
                    k--;
                else
                    continue;
            }
            if (c == ')')
                k++;
            s2.push_back(c);
        }
        std::string rev_s2(s2.rbegin(), s2.rend());
        return rev_s2;
    }
};
