class Solution(object):
    def maxProduct(self, nums):
        """
        动态规划
        nums会有负数，所以在保存最大值时如果遇到负数不做保存的话，后面如果有
        另一个负数，最大值就不对了，所以同时保存最大值和最小值
        :type nums: List[int]
        :rtype: int
        """
        maxvalue = minvalue = nums[0]
        globalmax = nums[0]
        for i in range(1,len(nums)):
            temp = maxvalue
            maxvalue = max(temp*nums[i],minvalue*nums[i],nums[i])
            minvalue = min(temp*nums[i],minvalue*nums[i],nums[i])
            globalmax = max(globalmax,maxvalue)
        return globalmax