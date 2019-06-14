class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()#关键在于先排序
        N,result = len(nums),[]
        for i in range(N):
            if i > 0 and nums[i] == nums[i-1]:#跳过相同的数字
                continue
            target = nums[i] * (-1)  # a + b = -c
            l,r = i+1,N-1
            while l < r:
                if nums[l] + nums[r] == target:
                    result.append([nums[i],nums[l],nums[r]])
                    l = l + 1
                    while l < r and nums[l] == nums[l-1]:#跳过相同的数字
                        l = l + 1
                elif nums[l] + nums[r] < target:
                    l = l + 1
                else:
                    r = r - 1
        return result


