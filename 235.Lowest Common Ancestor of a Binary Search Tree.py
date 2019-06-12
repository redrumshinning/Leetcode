# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            if max(p.val,q.val) < root.val:#最大的都小于root的值，说明在左边
                root = root.left
            elif min(p.val,q.val) > root.val:#最小的都大于root的值，说明在右边
                root = root.right
            else:#否则，说明左右各一个，或者有节点是root
                return root