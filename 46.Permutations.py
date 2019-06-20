class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        self.dfs(nums,[],ans)
        return ans

    def dfs(self,nums,path,ans):
        if not nums:
            ans.append(path)
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:],path+[nums[i]],ans)

S = Solution()
S.permute([1,2,3])
