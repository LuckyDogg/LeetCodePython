# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack=[]
        if root is not None:
            pNode =root
            num = root.val
        else:
            return False
        while pNode is not None or len(stack) != 0:
            if pNode!= None:
                if pNode.val == num:
                    stack.append(pNode)
                    pNode = pNode.left
                else:
                    return False
            else:
                node = stack.pop()
                pNode = node.right
        return True


if __name__ == '__main__':
     test=Solution()
     s = TreeNode(1)
     d = TreeNode(1)
     c = TreeNode(1)
     d.left = s
     d.right = c
     s.left = None
     s.right = None
     c.left = None
     c.right = None
     test.isUnivalTree(d)







