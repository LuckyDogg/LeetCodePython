class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        v = 0
        for firstindex in range(0,len(height)):
            for secondindex in range(firstindex+1,len(height)):
                temp = (secondindex - firstindex) * min(height[firstindex], height[secondindex])
                if temp > v:
                    v = temp
        return v