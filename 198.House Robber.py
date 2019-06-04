class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[-1]

    def rob2(self, nums):
        prev = curr = 0
        for num in nums:
          temp = prev # This represents the nums[i-2]th value
          prev = curr # This represents the nums[i-1]th value
          curr = max(num + temp, prev) # Here we just plug into the formula
        return curr

S = Solution()
print(S.rob2([2,4,1,5,7]))