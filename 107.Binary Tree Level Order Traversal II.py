# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:return []
        level = [root]
        queue = []
        queue.append([root.val])
        while level:
            valuelist = []
            temp = []
            for node in level:
                if node.left:
                    temp.append(node.left)
                    valuelist.append(node.left.val)
                if node.right:
                    temp.append(node.right)
                    valuelist.append(node.right.val)
            level = temp
            queue.insert(0,valuelist)
        return queue[1:]