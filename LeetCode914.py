class Solution:
    @staticmethod
    def gac(x,y):
        while y:
            x,y = y,x%y
        return x

    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        temp_dict={}
        templist=[]
        for num in deck:
            if num in temp_dict.keys():
                temp_dict[num] += 1
            else:
                temp_dict.setdefault(num,1)
        for count in temp_dict.values():
            templist.append(count)
        while len(templist) != 1:
            tempvalue=Solution.gac(templist[-1],templist[-2])
            templist.pop()
            templist.pop()
            templist.append(tempvalue)
        if templist[0]>1:
            return True
        else:
            return False

                


if __name__ == '__main__':
     test=Solution()
     s=[1,2,3,4,4,3,2,1]
     test.hasGroupsSizeX(s)
            
