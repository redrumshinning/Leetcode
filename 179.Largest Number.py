import functools

class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        compare = lambda a, b: 1 if a+b > b+a else -1 if a+b < b+a else 0
        nums = list(map(str, nums))
        nums.sort(key=functools.cmp_to_key(compare), reverse=True)#列表中元素逐一判断，例如11和2判断，112<211,所以11在前，2在后，最后再降序排列
        return str(int(''.join(nums)))


S = Solution()
print(S.largestNumber([11,2,13]))