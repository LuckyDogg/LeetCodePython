class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        o1 = [i for i in A if i % 2 == 0]
        o2 = [j for j in A if j % 2 == 1]
        return [i for j in zip(o1, o2) for i in j]


if __name__ == '__main__':
    t = Solution()
    S = [4,2,5,7]
    print(t.sortArrayByParityII(S))







