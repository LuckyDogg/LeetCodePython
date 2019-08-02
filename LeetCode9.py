class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        for i in range(int(len(x)/2)):
            if x[i] != x[-(i+1)]:
                return False
        return True

    def isPalindrome1(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        y = 0
        while x > y:
            y = y * 10 + x % 10
            x /= 10
        if x == y:
            return True
        else:
            y /= 10
            if x == y:
                return True
            else:
                return False



