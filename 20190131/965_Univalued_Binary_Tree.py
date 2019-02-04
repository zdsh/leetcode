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
        ret1 = True
        if root.left != None:
            if root.val != root.left.val:
               ret1 =  False
            else:
               ret1 = isUnivalTree(root.left)
        if root.right != None:
            if root.val != root.right.val:
                ret2 = False
            else:
               ret2 = isUnivalTree(root.rigt)
        return ret1 and ret2
        
