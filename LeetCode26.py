class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        j = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[j]:
                nums[j] = nums[i]
                j += 1

        return j

        def removeDuplicates(self, nums: List[int]) -> int:
            i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                nums[i + 1] = nums[j]
                i += 1
        return i + 1 if nums else 0



