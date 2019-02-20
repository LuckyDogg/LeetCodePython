class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return False
        if n % 2 == 1:
            n = (n-1)/2
        while n > 2:
            if n % 2 == 0:
                n = n/2
            else:
                return False
            if n % 2 == 1:
                n = (n-1)/2
            else:
                return False
        if n==2:
            return True
        else:
            return False


if __name__ == '__main__':
    s=Solution()
    d=11
    s.hasAlternatingBits(11)
