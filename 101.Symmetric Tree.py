# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            return self.isMirror(root.left,root.right)

    def isMirror(self,left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False

        if left.val == right.val:
            outNum = self.isMirror(left.left,right.right)
            inNum = self.isMirror(left.right,right.left)
            return outNum and inNum#不能用==，如果两个都是False就会返回True
        else:
            return False

    def isSymmetric2(self, root):
        def isSym(L,R):
            if not L and not R: return True
            if L and R and L.val == R.val:
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return False
        return isSym(root, root)

    def isSymmetric3(self, root):
        if root is None:
            return True

        stack = [[root.left, root.right]]

        while len(stack) > 0:
            pair = stack.pop(0)
            left = pair[0]
            right = pair[1]

            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.insert(0, [left.left, right.right])

                stack.insert(0, [left.right, right.left])
            else:
                return False
        return True