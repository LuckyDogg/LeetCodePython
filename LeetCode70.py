class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return False
        a=2
        b=1
        if n == 1:
            return 1
        elif n == 2:
            return 2
        for i in range(3, n+1):
            temp = a
            a += b
            b = temp
        return a

class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s : %s' % (self.name, self.score))


bart = Student('bart', 68)

lisa =Student('lisa', 90)

lisa.print_score()
bart.print_score()
