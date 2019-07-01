# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        关键在于preorder中第一个值为根节点，inorder左右子树在根节点两侧
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            index = inorder.index(preorder.pop(0))#或者直接写成 root=TreeNode(preorder(0))
            root = TreeNode(inorder[index])                   #index=inorder.index(root.val)
            root.left = self.buildTree(preorder,inorder[:index])
            root.right = self.buildTree(preorder,inorder[index+1:])
            return root