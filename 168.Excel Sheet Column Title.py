class Solution(object):
    def convertToTitle(self, n):
        result = ''
        distance = ord('A')

        while n > 0:
            y = (n - 1) % 26
            n = (n - 1) // 26
            s = chr(y + distance)
            result = ''.join((s, result))

        return result

    def convertToTitle2(self, num):
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while num > 0:
            result.append(capitals[(num-1)%26])
            num = (num-1) // 26
        result.reverse()
        return ''.join(result)
S = Solution()
print(S.convertToTitle(777))