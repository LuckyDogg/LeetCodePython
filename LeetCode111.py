# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def min_depth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        if root.left and root.right:
            left = self.min_depth(root.left)
            right = self.min_depth(root.right)
            return left+1 if right > left else right+1
        elif root.left:
            return self.min_depth(root.left)+1
        elif root.right:
            return self.min_depth(root.right)+1
        else:
            return 1