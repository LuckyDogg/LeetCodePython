class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        value=0
        alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        for num in s:
             value += alphabet.index(num)+1
        return value

