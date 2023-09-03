# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ary = []
        cur = head
        while cur: ary.append(cur.val); cur = cur.next
        if ary:
            head = ListNode(ary[0], None)
            for i in ary[1:]:
                newnode = ListNode(i, head)
                head = newnode
            return head
