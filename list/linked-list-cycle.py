#  https://leetcode.com/problems/linked-list-cycle/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        try:
            tortue = head
            lapin = head.next
            while lapin is not tortue:
                tortue = tortue.next
                lapin = lapin.next.next
            return True
        except AttributeError:
            return False

s = Solution()
list = ListNode(0)
assert not s.hasCycle(list)
list.next = ListNode(1)
list.next.next = ListNode(2)
assert not s.hasCycle(list)
list.next.next = list.next
assert s.hasCycle(list)
