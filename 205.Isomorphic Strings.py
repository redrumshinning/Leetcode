class Solution(object):
    def isIsomorphic(self, s, t):
        """
        利用字典，不同的值会保存不同的位置
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1, d2 = {}, {}
        for i, val in enumerate(s):
            d1[val] = d1.get(val,[]) + [i]#dic.get[val,[]]:如果没有dic[val]，那么返回[]
        for i, val in enumerate(t):
            d2[val] = d2.get(val,[]) + [i]
        return sorted(d1.values()) == sorted(d2.values())


    def isIsomorphic2(self, s, t):#Ascii码共256个
        d1, d2 = [[] for _ in range(256)], [[] for _ in range(256)]
        for i, val in enumerate(s):
            d1[ord(val)].append(i)
        for i, val in enumerate(t):
            d2[ord(val)].append(i)
        return sorted(d1) == sorted(d2)

    def isIsomorphic3(self, s, t):#zip(s,t)表示s与t配对，再去掉重复的对子，如果是一样的格式，len是相同的
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))

    def isIsomorphic4(self, s, t):#find会返回找到的第一个的值的索引，等于这个值的标记
        return [s.find(i) for i in s] == [t.find(j) for j in t]

    def isIsomorphic5(self, s, t):#同上一种方法，map会返回一个列表
        return map(s.find, s) == map(t.find, t)

    def isIsomorphic6(self, s, t):
        d1, d2 = [0 for _ in range(256)], [0 for _ in range(256)]
        for i in range(len(s)):
            if d1[ord(s[i])] != d2[ord(t[i])]:
                return False
            d1[ord(s[i])] = i + 1
            d2[ord(t[i])] = i + 1
        return True

S = Solution()
s1,s2= 'abba','cddc'
print(S.isIsomorphic2(s1,s2))
print()
