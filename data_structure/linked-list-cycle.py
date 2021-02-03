#  https://leetcode.com/problems/linked-list-cycle/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        def next(tortue, lapin):
            if lapin is None or lapin.next is None:
                return False
            tortue = tortue.next
            lapin = lapin.next.next
            return lapin is tortue or next(tortue, lapin)
        return next(head, head)

s = Solution()
list = ListNode(0)
list.next = ListNode(1)
list.next.next = ListNode(2)
assert not s.hasCycle(list)
list.next.next = list.next
assert s.hasCycle(list)
