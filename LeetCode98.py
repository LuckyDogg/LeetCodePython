# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    @staticmethod
    def isValidBST(root: TreeNode) -> bool:
        nodestack = []
        valnode = root
        vallist = []
        while valnode is not None or len(nodestack) > 0:
            if valnode is not None:
                nodestack.append(valnode)
                valnode = valnode.left
            else:
                valnode = nodestack.pop()
                vallist.append(valnode.val)
                valnode = valnode.right
                if len(vallist) > 1:
                    if vallist[-1] <= vallist[-2]:
                        return False
        return True




s1 = TreeNode(1)
s2 = TreeNode(2)
s3 = TreeNode(3)

s2.left = s1
s2.right = s3

if __name__ == '__main__':
    s = Solution.isValidBST(s2)
    print(s)
