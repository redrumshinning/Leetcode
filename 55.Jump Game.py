class Solution(object):#[2,3,1,1,4]   [3,2,1,0,4]
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stepsLeft = nums[0]

        if not stepsLeft and len(nums) > 1:
            return False

        for num in nums[1:-1]:
            stepsLeft = max(stepsLeft - 1, num)
            if not stepsLeft:
                return False

        return True

    def canJump2(self, nums):
        if len(nums) < 2:
            return True

        min_successful_index = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= min_successful_index:
                min_successful_index = i

        return min_successful_index == 0

