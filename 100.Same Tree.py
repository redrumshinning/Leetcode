# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return p == q  #可能p和q都为None，则返回True，或者其中一方为None，则返回False

    def isSameTree2(self, p, q):
        stack = [(p, q)]#将两个节点保存为元组，更加方便
        while stack:
            n1, n2 = stack.pop()
            if not n1 and not n2: continue
            if not n1 or not n2: return n1 == n2
            if n1.val != n2.val: return False
            stack.append((n1.right, n2.right))
            stack.append((n1.left, n2.left))
        return True

    def isSameTree3(self, p, q):
        queue = collections.deque([(p, q)])
        while queue:
            n1, n2 = queue.popleft()
            if not n1 and not n2: continue
            if not n1 or not n2: return n1 == n2
            if n1.val != n2.val: return False
            queue.append((n1.left, n2.left))
            queue.append((n1.right, n2.right))
        return True

a1 = TreeNode(1)
b1 = TreeNode(2)
c1 = TreeNode(3)
a1.left = b1
a1.right = c1

a2 = TreeNode(1)
b2 = TreeNode(2)
c2 = TreeNode(3)
a2.left = b2
a2.right = c2

q = Solution()
print(q.isSameTree(a1,a2))
