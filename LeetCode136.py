class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a= 0
        for i in nums:
            a= a^ i
        return a