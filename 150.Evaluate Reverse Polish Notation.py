class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token in ('+','-','*','/'):
                a2 = stack.pop()
                a1 = stack.pop()
                result = self.doMath(token, int(a1), int(a2))
                stack.append(result)
            else:
                stack.append(token)
        return stack.pop()

    def doMath(self, operator, a1, a2):
        if operator == '+':
            return a1 + a2
        elif operator == '-':
            return a1 - a2
        elif operator == '*':
            return a1 * a2
        else:
            if a1 * a2 < 0 and a1 % a2 != 0:
                return a1 / a2 + 1 #如果a1绝对值小于a2的绝对值，商一定为-1，根据题意应该为0，所以加1
            else:
                return a1 / a2

S = Solution()
print(S.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
print(divmod(-5,6))
print(divmod(6,-132))
