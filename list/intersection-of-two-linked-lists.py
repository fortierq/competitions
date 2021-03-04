# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, i, headA: ListNode, headB: ListNode) -> ListNode:
        stackA = []
        stackB = []
        while headA:
            stackA.append(headA.val)
            headA = headA.next
        while headB:
            stackB.append(headB.val)
            headB = headB.next
        
        last = None
        while stackA and stackB:
            if stackA[-1] != stackB[-1]:
                return last
            last = stackA.pop()
            stackB.pop()
