class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        pile = []
        for c in s:
            if c == '(':
                pile.append(c)
            else:
                next = 0
                while pile[-1] != '(':
                    next += pile.pop()
                pile.pop()
                pile.append(max(1, 2*next))
        return sum(pile)
