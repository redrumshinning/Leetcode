# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:return False
        if not root.left and not root.right and root.val == sum:
            return True
        sum -= root.val

        return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)

    #   递归DFS
    def hasPathSum2(self,root,sum):
        res = []
        self.dfs(root,sum,res)
        return any(res)

    def dfs(self,root,sum,res):
        if root:
            if not root.left and not root.right:
                if root.val == sum:
                    res.append(True)

            if root.left:
                self.dfs(root.left,sum-root.val,res)
            if root.right:
                self.dfs(root.right,sum-root.val,res)

    #栈DFS
    def hasPathSum3(self,root,sum):
        if not root:return False
        stack = [(root,root.val)]
        while stack:
            curr,val = stack.pop()
            if not curr.left and not curr.right:
                if val == sum:
                    return True
            if curr.left:
                stack.append((curr.left,val+curr.left.val))
            if curr.right:
                stack.append((curr.right,val+curr.right.val))
        return False

    # BFS
    def hasPathSum4(self,root,sum):
        if not root:return False
        queue = [(root,sum-root.val)]
        while queue:
            curr,val = queue.pop(0)
            if not curr.left and not curr.right:
                if val == 0:
                    return True
            if curr.left:
                queue.append((curr.left,val-curr.left.val))
            if curr.right:
                queue.append((curr.right,val-curr.right.val))
        return False




