# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        vallist = []
        vallist.append((l1.val + l2.val) % 10)
        temp = (l1.val + l2.val) // 10
        l1Node = l1.next
        l2Node = l2.next
        while l2Node is not None and l1Node is not None:
            vallist.append((l1Node.val + l2Node.val + temp) % 10)
            temp = (l1Node.val + l2Node.val + temp) // 10
            l1Node = l1Node.next
            l2Node = l2Node.next

        if l2Node is not None:
            tempnode = l2Node
        elif l1Node is not None:
            tempnode = l1Node
        else:
            tempnode = None
        while tempnode is not None:
            vallist.append((tempnode.val + temp) % 10)
            temp = (tempnode.val + temp) // 10
            print(temp)
            tempnode = tempnode.next
        if temp != 0:
            vallist.append(temp)

        return vallist
