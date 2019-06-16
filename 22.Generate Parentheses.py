class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans

    def generateParenthesis2(self, n):
        if not n:
            return []
        left,right,ans = n,n,[]
        self.dfs(left,right,ans,'')
        return ans

    def dfs(self,left,right,ans,string):
        if left > right:#递归出口1：左必须小于右，意味着必须先有足够的左括号才能加右括号
            return
        if not left and not right:#递归出口2：当左和右为0时，将string保存
            ans.append(string)
            return
        if left:
            self.dfs(left-1,right,ans,string+"(")
        if right:
            self.dfs(left,right-1,ans,string+")")


S = Solution()
print(S.generateParenthesis2(2))
