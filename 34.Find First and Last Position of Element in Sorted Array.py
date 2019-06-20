class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if nums[i] == target:
                leftindex = i
                break
        else:
            return [-1,-1]

        for i in range(len(nums)-1,-1,-1):
            if nums[i] == target:
                rightindex = i
                break

        return [leftindex,rightindex]

    def searchRange(self, nums, target):
        low,high = 0,len(nums)-1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                left,right = mid ,mid
                while left >= low and nums[left] == target:
                    left -= 1
                while right <= high and nums[right] == target:
                    right += 1
                return [left+1,right-1]

            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return [-1,-1]
