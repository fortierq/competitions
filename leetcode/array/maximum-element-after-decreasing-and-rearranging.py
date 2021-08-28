def maximumElementAfterDecrementingAndRearranging(self, A):
    A.sort()
    pre = 0
    for a in A:
        pre = min(pre + 1, a)
    return pre
