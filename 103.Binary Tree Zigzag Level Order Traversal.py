# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:return []
        res = []
        level = [root]
        traversal = 1#在102题的基础上，每次赋值时反向就完事了
        while level:
            res.append([node.val for node in level][::traversal])
            pairs = [(node.left,node.right) for node in level]
            level = [node for pair in pairs for node in pair if node]
            traversal *= -1
        return res