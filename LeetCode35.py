class Solution:
    def searchInsert(self, nums, target: int) -> int:
        def iter_find(nums, low: int, high: int):
            mid = int((low + high)/2)
            if high > low+1:
                if nums[mid] < target:
                    low = mid+1
                    iter_find(nums, low, high)
                if nums[mid] > target:
                    high = mid-1
                    iter_find(nums, low, high)
                if nums[mid] == target:
                    return mid
            else:
                return high

        return iter_find(nums, 0, len(nums))


s1 = [1, 3, 5, 6]
target = 2

if __name__ == '__main__':
    s = Solution()
    d = s.searchInsert(s1, target)
    print(d)