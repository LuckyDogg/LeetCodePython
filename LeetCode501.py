# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> list[int]:
        nodelist = []
        vallist = []
        varnode = root
        while varnode is not None or len(nodelist) > 0:
            if varnode is not None:
                nodelist.append(varnode)
                varnode = varnode.left
            else:
                varnode = nodelist.pop()

                varnode = varnode.right




