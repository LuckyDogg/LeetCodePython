import re
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        l = re.match(r'L',moves)
        r = re.match(r'R',moves)
        u = re.match(r'U',moves)
        d = re.match(r'D', moves)
        print(len(l))
        print(len(u))
        if len(l)==len(r) and len(u) == len(d):
            return True
        else:
            return False



if __name__== '__main__':
    moves = 'UD'
    s =Solution()
    s.judgeCircle(moves)