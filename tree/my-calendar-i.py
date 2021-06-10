class MyCalendar:
    def __init__(self):
        self.bst = None

    def book(self, start: int, end: int) -> bool:
        if not self.bst:
            self.bst = BST((start, end))
            return True
        return self.bst.add((start, end))
            

class BST:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
    
    def add(self, val):
        if self.val is None:
            self.val = val
            return True
        I = self.val
        print(val, I)
        if val[0] < I[1] and I[0] < val[1]:
            return False
        if val < self.val:
            if not self.left:
                self.left = BST(val)
            else:
                return self.left.add(val)
        elif not self.right:
            self.right = BST(val)
        else:
            return self.right.add(val)
        return True
