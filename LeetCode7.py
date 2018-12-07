class Solution:
    def reverse(self,x):
        if -10 < x < 10:
            return x
        x = str(x)
        if x[0] != '-':
            x = x[::-1]
            x = int(x)
        else:
            x =x[1:][::-1]
            x = int(x)
            x = -x
        return x if -2147483648 < x < 2147483647 else 0