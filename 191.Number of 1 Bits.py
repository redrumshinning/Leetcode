class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')

    def hammingWeight2(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c

    def hammingWeight3(self, n):#4ms
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            if n & 1 == 1:
                count += 1
                n >>= 1
            else:
                n >>= 1
        return count

S = Solution()
a = 15
print(S.hammingWeight3(a))

