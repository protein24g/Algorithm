class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head
            prev.next = b
            head = head.next
            prev = prev.next.next
        return root.next
