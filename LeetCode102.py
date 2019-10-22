# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if root is not None:
            queue = [root]
            val_list = []
            while len(queue) > 0:
                child_list = []
                node_list = []
                for i in queue:
                    child_list.append(i.val)
                    if i.left is not None:
                        node_list.append(i.left)
                    if i.right is not None:
                        node_list.append(i.right)
                queue = node_list.copy()
                val_list.append(child_list)
            return val_list

