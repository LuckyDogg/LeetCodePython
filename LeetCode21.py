# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        headnode = tempnode = ListNode(0)
        while l1 and l2 :
            if l1.val < l2.val:
                tempnode.next = l1
                l1 = l1.next
            else:
                tempnode.next = l2
                l2 = l2.next
            tempnode = tempnode.next

        tempnode.next = l1 if l1 else l2

        return headnode.next

















