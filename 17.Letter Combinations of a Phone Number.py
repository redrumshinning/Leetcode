class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        elif len(digits) == 1:#递归退出条件为只剩一个数字时
            return dic[digits]
        else:
            pre = self.letterCombinations(digits[:-1])
            add = dic[digits[-1]]  #得到当前digits的最后一个数字
            return [s + l for s in pre for l in add]

S = Solution()
print(S.letterCombinations('234'))