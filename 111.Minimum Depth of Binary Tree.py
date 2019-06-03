# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        level = [root]
        depth = 0
        while level:
            queue = []
            depth += 1
            for node in level:
                if not node: continue
                if node.left or node.right:
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    return depth

            level = queue


    # DFS
    def minDepth1(self, root):
        if not root:
            return 0
        if None in [root.left, root.right]:
            return max(self.minDepth1(root.left), self.minDepth1(root.right)) + 1
        else:
            return min(self.minDepth1(root.left), self.minDepth1(root.right)) + 1


    # BFS
    def minDepth2(self, root):
        if not root:
            return 0
        queue = collections.deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if node:
                if not node.left and not node.right:
                    return level
                else:
                    queue.append((node.left, level + 1))
                    queue.append((node.right, level + 1))


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
b.left = f
a.right = c
c.left = d
c.right = e

S = Solution()
print(S.minDepth(a))