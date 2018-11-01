class Solution:
    def nextGreatestLetter(self,letters,target):
        stringArray = [i for i in letters if ord(i) > ord(target)]
        if(stringArray):
            return stringArray[0]
        else:
            return letters[0]