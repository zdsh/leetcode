"""
File: 872_Leaf-Similar_Trees.py
Date: 2019/02/22 15:11:39
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def getleafs(root):
            stack, leafValues = [], []
            if root.left == None and root.right == None:
                return [root.val]
            ret = []
            if root.left:
                ret += getleafs(root.left)
            if root.right:
                ret += getleafs(root.right)
            return ret
        return getleafs(root1) == getleafs(root2)
