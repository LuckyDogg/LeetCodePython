import re


class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        pattern = re.compile(r'\w+')   # 查找单词
        result = pattern.findall(paragraph.lower())
        # result=list(paragraph)
        newlist = []
        newcount = []
        for i in result:
            if(i not in newlist):
                if(i not in banned):
                    newlist.append(i)
        for i in newlist:
            newcount.append(result.count(i))
        return newlist[newcount.index(max(newcount))]
