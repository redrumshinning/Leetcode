class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}

        for value in nums:
            if value in dic:
                return True
            else:
                dic[value] = 1
        return False

    def containsDuplicate2(self, nums):
        return len(set(nums)) != len(nums)