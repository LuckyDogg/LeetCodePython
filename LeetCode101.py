# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # print(root.val)

        def iter_test(left: TreeNode, right:TreeNode):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            return iter_test(left.right,right.left) and iter_test(left.left, right.right) and left.val == right.val

        return iter_test(root, root)









l = [1,2,2,2,None,2]

node = TreeNode(l[0])
node.left = TreeNode(l[1])
node.right =TreeNode(l[2])
node.left.left =TreeNode(l[3])
node.left.right =TreeNode(l[4])
node.right.left =TreeNode(l[5])
# node.right.right =TreeNode(l[6])
# node.left.right.left = TreeNode(4)
# node.right.left.right=TreeNode(4)

if __name__ == '__main__':
    s = Solution()
    s.isSymmetric(node)