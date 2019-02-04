"""
File: 965_Univalued_Binary_Tree.py
Date: 2019/02/04 11:18:47
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        if root.left != None and root.val != root.left.val:
            return False
        if root.right != None and root.val != root.right.val:
            return False
        return True
        
