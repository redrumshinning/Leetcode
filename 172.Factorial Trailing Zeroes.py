#判断某个数的阶乘末尾有几个0，可以看作阶乘运算中有几对2*5，由于2的个数远远多于5，
#所以只需求出5的个数，但是还会有25,75等包含两个5或多个5的数字，所以利用递归除以一个5等于把
#有5的全求出来，再除5等于把25的求出来，以此类推
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)

    def trailingZeroes2(self, n):#非递归
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count

S = Solution()
print(S.trailingZeroes(100))