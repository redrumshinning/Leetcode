# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth2(self, root):
        if not root: return 0

        left = self.maxDepth2(root.left)
        right = self.maxDepth2(root.right)
        return max(left, right) + 1

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level = []
        if root:
            level.append(root)
        else:
            return 0
        depth = 0
        while level:
            depth += 1
            queue = []
            for node in level:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            #level = queue 放在这里运行速度就会慢很多，不知道为啥
                level = queue
                print(level)

        return depth

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
h = TreeNode(8)
i = TreeNode(9)
j = TreeNode(10)
a.left = b
a.right = c
b.left = d
b.right = e
d.left = g
g.left = h
e.left = f
c.left = i
c.right = j
S = Solution()
print(S.maxDepth(a))
