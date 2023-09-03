class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a1, a2 = '', ''
        cur = l1
        while cur: a1 += str(cur.val); cur = cur.next
        a1 = list(a1); a1.reverse(); a1 = ''.join(a1)

        cur = l2
        while cur: a2 += str(cur.val); cur = cur.next
        a2 = list(a2); a2.reverse(); a2 = ''.join(a2)

        res = str(int(a1) + int(a2))
        if res[0] == '0' and len(res) == 1:
            head = ListNode()
        else:
            head = ListNode(res[0], None)
            for i in res[1:]:
                newnode = ListNode(i, head)
                head = newnode
        return head
