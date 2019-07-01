# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node,lower,upper):
            if not node:return True
            if node.val <= lower or node.val >= upper:
                return False
            left = helper(node.left,lower,node.val)
            right = helper(node.right,node.val,upper)
            return left and right
        return helper(root,-float('inf'),float('inf'))

    def isValidBST2(self, root):#中序遍历保存所有值在比较
        self.arr = []
        self.inorder(root)
        return self.arr == sorted(self.arr) and len(self.arr) == len(set(self.arr))

    def inorder(self, root):
        if not root: return
        self.inorder(root.left)
        self.arr.append(root.val)
        self.inorder(root.right)
############################################
    def isValidBST3(self, root):
        self.last = -float('inf')
        self.flag = True
        self.inorder(root)
        return self.flag

    def inorder(self, root):
        if not root: return
        self.inorder(root.left)#先判断该节点的左子树是否大于最小值，再保存该节点的值最为最小值，
        if self.last >= root.val:#再判断该节点的值是否大于右子树的值
            self.flag = False
        self.last = root.val
        self.inorder(root.right)


