class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 1
        for num in range(3, n):
            for i in range(2, int(num/2)):
                i = 2
                if num % i == 0:
                    break
            count += 1
            print(num)
        return count


if __name__ == '__main__':
     test = Solution()
     s = 10
     test.countPrimes(s)
