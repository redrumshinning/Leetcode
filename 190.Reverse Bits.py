class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        oribin='{0:032b}'.format(n)
        reversebin=oribin[::-1]
        return int(reversebin,2)

    def reverseBits2(self, n):
        '''
        该题主要考察位运算。由于限制位数为32位，所以只需对待处理的整数n进行32次右移位，
        每当低位&1的结果为1，说明低位为1，此时将待输出的目标整数(默认值为0)左移动一位并加上1；
        每当低位&1的结果为0，说明低位为0，此时将待输出的目标整数左移一位即可；循环直到移动完32次，
        所得目标整数即为所求。
        '''
        ans = 0
        for i in range(32):
            ans = (ans << 1) + (n & 1)
            print(bin(ans))
            n >>= 1
            print(bin(n))
        return ans

S = Solution()
a = 60
print(S.reverseBits2(a))




