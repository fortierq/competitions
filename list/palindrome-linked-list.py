# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        cur = head
        L = []
        while cur:
            L.append(cur.val)
            cur = cur.next
        return L == L[::-1]
