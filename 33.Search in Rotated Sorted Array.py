class Solution(object):
    def search(self, nums, target):
        """
        因为是排序的列表再翻转，就要考虑到几种情况
        比如[0,1,2,3,4,5,6]旋转后有两种情况
        1.[4,5,6,0,1,2,3]
        2.[3,4,5,6,0,1,2]
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        low, high = 0,len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1