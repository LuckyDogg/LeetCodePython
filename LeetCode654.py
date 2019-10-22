# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode:
        numlist = sorted(nums)
        headnode = TreeNode(numlist.pop())
        prenode = headnode
        while len(numlist) > 0:
            val = numlist.pop()











