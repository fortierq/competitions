class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0: return False
        n = 0
        for i, c in enumerate(s):
            if locked[i] == '1' and c == ')':
                n +=1
            if n > (i + 1) // 2:
                return False
        n = 0
        locked = locked[::-1]
        for i, c in enumerate(s[::-1]):
            if locked[i] == '1' and c == '(':
                n +=1
            if n > (i + 1) // 2:
                return False
        return True