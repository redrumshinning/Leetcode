class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        # handle condition 3
        while left < right - 1:
            mid = (left + right) / 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1

        # handle condition 1 and 2
        return left if nums[left] >= nums[right] else right


    def findPeakElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [1,2,1,3,5,6,4]
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            if left == right:
                return left
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

S = Solution()
print(S.findPeakElement2([1,2,1,3,5,6,4]))



