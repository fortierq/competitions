from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        digits = list(map(Counter, ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]))
        s = Counter(s)
        res = []
        i = 0
        while i < len(digits):
            d = digits[i]
            try:
                for k in d:
                    if d[k] > s[k]:
                        raise Exception
                s.subtract(d)
                res.append(str(i))
            except Exception:
                i += 1
        return ''.join(res)
