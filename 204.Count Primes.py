class Solution(object):
    def countPrimes(self, n):
        """
        厄拉多塞筛法,a[i * i: n : i]等于取间隔为i的[i:n]的所有值，
        对于N来说，不必用从2到N一1的所有素数去除，只需用小于等于√N(根号N)的所有素数去除就可以了。
        这一点可以用反证法来证明：如果N是合数，则一定存在大于1小于N的整数d1和d2，使得N=d1×d2。
        如果d1和d2均大于√N，则有：N＝d1×d2>√N×√N＝N。而这是不可能的，
        所以，d1和d2中必有一个小于或等于√N。
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        Eratos = [True] * n
        Eratos[0] = Eratos[1] = False
        for i in range(2,int(n**0.5)+1):
            if Eratos[i]:
                Eratos[i*i:n:i] = [False]*len(Eratos[i*i:n:i])
        return sum(Eratos)

S = Solution()
print(S.countPrimes(100))
