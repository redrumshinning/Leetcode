class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in nums:
            if i in dic:
                dic.pop(i)
            else:
                dic[i] = 1
        return dic.popitem()[0]

    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #from functools import reduce  python3
        #return reduce(lambda x, y: x ^ y, nums)
        #return reduce(operator.xor, nums)
        a = 0
        for i in nums:
            a ^= i # ^为异或符号，将其转化为二进制后，相等为0，不等为1，运算可以交换位置，a^b^a=b例如：a=0，i=2,
        return a  #                                                        0 =  0  0      1  0
                   #                                                        2 =  1  0      1  0
                   #                                                             1  0      0  0

    def singleNumber3(self, nums):#2∗(a+b+c)−(a+a+b+b+c)=c
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)