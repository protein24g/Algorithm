class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        ary = []
        node = list1
        while node:
            ary.append(node.val)
            node = node.next
        node = list2
        while node:
            ary.append(node.val)
            node = node.next
        ary = list(sorted(ary))
        if ary:
            tmp = ary[0]
            head = ListNode(tmp, None)
            cur = head
            for i in ary[1:]:
                newnode = ListNode(i, None)
                while cur.next: cur = cur.next
                cur.next = newnode
            return head
            
