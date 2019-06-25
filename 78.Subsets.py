class Solution(object):#[1,2,3,4]
    def subsets(self, nums):
        """
        做的时候没有加index，导致产生了所有排序，比如[1,2]和[2,1]等
        def dfs(self, nums, path, res):
            res.append(path)
            for i in range(index, len(nums)):
                self.dfs(nums[0:i]+nums[I+1:], path + [nums[i]], res)
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        print(res)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]], res)

    def subsets2(self, nums):
        """
        BFS method
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        all_subsets = [[]]
        if not nums:
            return all_subsets
        for num in nums:
            for idx in range(len(all_subsets)):
                all_subsets.append(all_subsets[idx] + [num])
        return all_subsets
    # Bit Manipulation
    def subsets3(self, nums):
        res = []
        nums.sort()
        for i in range(1<<len(nums)):
            tmp = []
            for j in range(len(nums)):
                if i & 1 << j:  # if i >> j & 1:
                    tmp.append(nums[j])
            res.append(tmp)
        return res

S = Solution()
print(S.subsets3([1,2,3]))
print(2&1<<1)