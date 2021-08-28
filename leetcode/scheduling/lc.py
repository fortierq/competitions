class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        expression = expression[::-1]
        def par(i, j):
            p = 0
            for k in range(i+1, j+1):
                if k == j:
                    return -1
                if expression[k] == ')':
                    if p == 0: 
                        return k
                    p-=1
                if expression[k] == '(':
                    p+=1   
            
        def f(i, j):
            if i == j:
                return 1, expression[i] == '1'
            
            k = i + 1
            if expression[i] == '(':
                k = par(i, j)
                if k == -1:
                    return f(i+1, j-1)
                k+=1
                
            if expression[k] == '|':
                n1, b1 = f(i, k-1)
                n2, b2 = f(k+1, j)
                if b1 or b2:
                    if b1 and b2:
                        return 1 + min(n1,n2), True
                    return 1, True
                    
                return min(n1,n2), False
            
            if expression[k] == '&':
                n1, b1 = f(i, k-1)
                n2, b2 = f(k+1, j)
                if b1 and b2:
                    return min(n1,n2), True
                if b1 or b2:
                    return 1, False
                return 1 + min(n1,n2), False
            
        return f(0, len(expression)-1)[0]

S = Solution()
S.minOperationsToFlip("1|1|(0&0)&1")
