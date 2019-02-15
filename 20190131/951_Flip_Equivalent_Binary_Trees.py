"""
File: 951_Flip_Equivalent_Binary_Trees.py
Date: 2019/02/16 03:17:02
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        if root1.val != root2.val:
            return False
        ret_1 = self.flipEquiv(root1.left, root2.left) \
                   and self.flipEquiv(root1.right, root2.right)
        
        ret_2 = self.flipEquiv(root1.left, root2.right) \
                   and self.flipEquiv(root1.right, root2.left)
        return ret_1 or ret_2
