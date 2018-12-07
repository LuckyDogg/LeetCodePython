class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<3:
            return 1==1
        else:
            return n%2==1