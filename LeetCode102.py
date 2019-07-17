# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        stack = []
        if root is None:
            return []

        l = []
        def treelevel(root:TreeNode):
            if root is not None:
                l.append(root.val)
                if root.left is not None:
                    stack.append(root.left)
                if root.right is not None:
                    stack.append(root.right)
                while len(stack) != 0:
                    temp = stack.pop()
                    l.append(temp.val)
                    if temp.left is not None:
                        stack.append(temp.left)
                    if temp.right is not None:
                        stack.append(temp.right)

                return l
        l = treelevel(root)
        return l


nodelist=[]
def Tree(l):

    def l():
        while len(nodelist)!=0:

