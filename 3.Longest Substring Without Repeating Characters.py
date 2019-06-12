class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        q = ''
        p = ''

        for i in s:
            if i not in p:
                p += i
            else:
                if len(p) > len(q):
                    q = p
                p = p[p.index(i) + 1:] + i

        return max(len(q), len(p))

    def lengthOfLongestSubstring2(self, s):
        dic = {}
        maxLength = start = 0
        for i,v in enumerate(s):
            if v in dic and start <= dic[v]:#满足v已经在前面出现并且起始位置要小于等于v的索引
                start = dic[v] + 1
            else:
                maxLength = max(maxLength,i - start + 1)

            dic[v] = i
            print(dic,start,maxLength)
        return maxLength

S = Solution()
print(S.lengthOfLongestSubstring2("tmmzuxt"))