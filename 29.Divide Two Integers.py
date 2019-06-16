class Solution:
    # @return an integer
    '''
    第一时间想到的求商的方法是累加法，比如10/3,sub=10-3=7，count+1，直到sub小于0
    以下的方法加速了这一过程，首先减去一个3，然后temp=3*2=6，i=1*2，表示两个3，
    ，比累加法速度更快
    '''
    def divide(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)#注意这里是is，同号为True
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:#注意等于号
            temp, i = divisor, 1
            while dividend >= temp:#注意等于号
                dividend -= temp
                res += i
                i <<= 1 # 左移一位等同于i*2
                temp <<= 1 #等同于temp*2
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)#min(max(-2**31,res),2**31-1)

S = Solution()
print(S.divide(7,3))
