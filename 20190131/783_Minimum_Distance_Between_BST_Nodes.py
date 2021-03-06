"""
File: 783_Minimum_Distance_Between_BST_Nodes.py
Date: 2019/02/28 22:26:15
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inorder(root):
            ret = []
            if root.left:
                ret += inorder(root.left)
            ret += [root.val]
            if root.right:
                ret += inorder(root.right)
            return ret
        values = inorder(root)
        return min([abs(values[i+1] - values[i]) for i in range(0, len(values) - 1)])       

