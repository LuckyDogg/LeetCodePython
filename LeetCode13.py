class Solution:
    def romanToInt(self, s: str) -> int:
        numdict={
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        if len(s) == 0:
            return None
        data = 0
        for i in range(0, len(s)):
            try:
                if s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X'):
                    data -= 1
                elif s[i] == 'X' and (s[i+1] == 'L' or s[i+1] == 'C'):
                    data -= 10
                elif s[i] == 'C' and (s[i+1] == 'D' or s[i+1] == 'M'):
                    data -= 100
                else:
                    data += numdict[s[i]]
            except:
                data += numdict[s[i]]

        return data


if __name__ == '__main__':
    s=Solution()
    tempstr='XC'
    print(s.romanToInt(tempstr))







