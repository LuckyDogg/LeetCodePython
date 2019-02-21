class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        j = 0
        for i in nums:
            b = nums.index(i)
            nums.remove(i)
            j += 1
            if target-i in nums:
                print([b, nums.index(target-i)+j])
                return [b, nums.index(target-i)+j]


if __name__ == "__main__":
    test = Solution()
    test.twoSum([3, 2, 3], 6)
