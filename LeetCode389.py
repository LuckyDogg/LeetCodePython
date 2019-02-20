class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for i in s:
            print(i)
            t = t.replace(str(i), '', 1)
        print(t)
        return t

if __name__ == '__main__':
     test = Solution()
     s='abcd'
     t='abcde'
     test.findTheDifference(s, t)