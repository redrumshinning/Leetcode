class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:return False
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        print(dic)
        for num in dic:
            print(dic[num])
            if dic[num] > (len(nums)//2):
                return num
        return False

    def majorityElement2(self, nums):#某个数字重复超过一半，排序后中间值必为此数
        nums.sort()
        return nums[len(nums) // 2]

    def majorityElement3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 遇到相同的数字计数，如果遇到不同的就减计数，直到计数为0，相当于把相同个数的数字都减去了，最终剩下的就为最多的
        # the idea here is if a pair of elements from the
        # list is not the same, then delete both, the last
        # remaining element is the majority number
        count, cand = 0, 0
        for num in nums:
            if num == cand:
                count += 1
            elif count == 0:
                cand, count = num, 1
            else:
                count -= 1
        return cand

S = Solution()
print(S.majorityElement3([2,2,1,1,1,2,2]))