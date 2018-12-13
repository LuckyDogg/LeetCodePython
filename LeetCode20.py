class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        dict={'[':']','{':'}','(':')'}
        for i in s:
            if len(stack) == 0:
                if i in dict.values():
                    return False
            if i in dict.keys():
                stack.append(i)
            else:
                if dict[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False


s=Solution();
print(s.isValid("[([]])"))
