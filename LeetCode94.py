# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        varnode = root
        node_stack = []
        vallist = []
        while varnode is not None or len(node_stack) > 0:
            if varnode is not None:
                node_stack.append(varnode)
                varnode = varnode.left
            else:
                varnode = node_stack.pop()
                vallist.append(varnode.val)
                varnode = varnode.right
        return vallist













