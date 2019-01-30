class Solution:
    def wordPattern(self,pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        try:
            num = ord(pattern[0:1])
        except:
            return False
        prepattern = ''
        str = str.split(' ')
        l = {}
        for i in str:
            if i not in l.keys():
                l.setdefault(i, chr(num))
                num += 1
            prepattern += l[i]

        if prepattern == pattern:
            return True
        else:
            return False