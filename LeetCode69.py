class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 1
        while x > 0:
            x -= i
            i += 2
        if x == 0:
            return int((i+1)/2-1)
        else:
            return int((i+1)/2-2)

