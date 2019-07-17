# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = l1 if l1.val < l2.val else l2
        l = head

        while l1.next is not None or l2.next is not None:
            if l1.next.val < l2.next.val:
                head.next = l1.next
                l1.next = l1.next.next
            else:
                head.next = l2.next.val
                l2.next = l2.next.next

            head = head.next

        if l1.next is None:
            head.next=l2.next
        else:
            head.next=l1.next
        print(l)
        return lambda x: for i in range(1,100)
        return l










