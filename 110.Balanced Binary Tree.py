# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#参考104题，利用getheight分别求得左右树的高度，然后递归调用分别判断每颗树是否是平衡的
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        left = self.getheight(root.left)
        right = self.getheight(root.right)
        if abs(left - right) > 1: return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def getheight(self, root):
        if not root: return 0
        left = self.getheight(root.left)
        right = self.getheight(root.right)

        return max(left, right) + 1


class Solution2(object):#不用求得每棵树的高度，只要>1就可以返回-1，代表这棵树不平衡
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        height = self.getheight(root)
        return height != -1

    def getheight(self, root):
        if not root: return 0
        left = self.getheight(root.left)
        right = self.getheight(root.right)
        if left == -1 or right == -1: return -1
        if abs(left - right) > 1: return -1
        return max(left, right) + 1
