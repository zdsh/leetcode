"""
File: 938_Range_Sum_of_BST.py
Date: 2019/02/17 11:25:34
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        ret = 0
        if root.left:
            ret += self.rangeSumBST(root.left, L, R)
        if root.right:
            ret += self.rangeSumBST(root.right, L, R)
        if root.val >= L and root.val <= R:
            ret += root.val
        return ret
