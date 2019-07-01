# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:return []
        res = []
        level = [root]
        while level:
            res.append([node.val for node in level])
            pairs = [(node.left,node.right) for node in level]
            level = [node for pair in pairs for node in pair if node]
        return res