class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return  sorted(list(map(lambda x: x * x, A)))


if __name__ == "__main__":
    arr = [-4,-1,0,3,10]
    t = Solution()
    print(t.sortedSquares(arr))