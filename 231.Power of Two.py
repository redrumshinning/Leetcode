class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0:
            return False
        else:
            a = list(bin(n))
            return a.count('1') == 1

    def isPowerOfTwo2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 1:
            return n == 1
        while n > 1:
            n, q = divmod(n, 2)
            if q:
                return False
        return True

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not (n & n-1)

S = Solution()
print(S.isPowerOfTwo(16))
