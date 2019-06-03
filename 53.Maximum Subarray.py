#不管哪种方法，核心思想就是列表中当前值加上前面加起来的值比较，如果大于前面的值（说明当前值为正数），则加上
def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
        print(nums)
    return max(nums)

def maxSubArray2(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        if dp[i - 1] > 0:
            dp[i] = dp[i - 1] + nums[i]
        else:
            dp[i] = nums[i]
        print(dp)
    return max(dp)

def maxSubArray3(nums):
    res = before = nums[0]
    for num in nums[1:]:
        if before >= 0:
            before = before + num
        else:
            before = num
        if res < before:
            res = before
    return res

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))