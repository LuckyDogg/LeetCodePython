class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        n = str(bin(n).replace('b', ''))
        return len(n.replace(str(0), ''))



if __name__ == '__main__':
    s= Solution()
    s.hammingWeight(0b00000000000000000000000000001011)