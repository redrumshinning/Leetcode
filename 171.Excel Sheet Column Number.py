from functools import reduce
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1]
        sum = 0
        for index,value in enumerate(s):
            sum += (ord(value) - 65 + 1) * pow(26,index)
        return sum

    def titleToNumber2(self, s):#map内通过函数映射得到列表，reduce用来依次累加数值
        return reduce(lambda x, y: x * 26 + y, map(lambda x: ord(x) - ord('A') + 1, s))

S = Solution()
print(S.titleToNumber2('ACD'))