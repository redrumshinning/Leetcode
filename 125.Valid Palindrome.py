class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newS= [i.lower() for i in s if i.isalnum()]
        return newS == newS[::-1]

