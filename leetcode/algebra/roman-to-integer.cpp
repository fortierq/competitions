#include <string>
#include <iostream>

using namespace std;

class Solution
{
public:
    int val(char c)
    {
        if (c == 'I')
            return 1;
        else if (c == 'V')
            return 5;
        else if (c == 'X')
            return 10;
        else if (c == 'L')
            return 50;
        else if (c == 'C')
            return 100;
        else if (c == 'D')
            return 500;
        else if (c == 'M')
            return 1000;
        return -1;
    }

    int romanToInt(string s)
    {
        int total = 0;
        int i = 0;
        for (; i < s.length() - 1; i++)
        {
            string s2 = s.substr(i, 2);
            if (s2 == "IV")
                total += 4;
            else if (s2 == "IX")
                total += 9;
            else if (s2 == "XL")
                total += 40;
            else if (s2 == "XC")
                total += 90;
            else if (s2 == "CD")
                total += 400;
            else if (s2 == "CM")
                total += 900;
            else
            {
                total += val(s[i]);
                continue;
            }
            i += 1;
        }
        if (i < s.length())
            total += val(s[i]);
        return total;
    }
};

int main(int argc, char **argv)
{
    Solution s = Solution();
    cout << s.romanToInt("MCMXCIV") << endl;
    cout << s.romanToInt("III") << endl;
}
