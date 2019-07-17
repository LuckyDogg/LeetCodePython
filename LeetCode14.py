class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        tmps=''
        try:
            for i in range(len(strs[0])):
                s = strs[0][i]
                for j in strs[1:]:
                    if j[i] != s:
                        return tmps
                tmps += s
            return tmps
        except:
            return tmps



