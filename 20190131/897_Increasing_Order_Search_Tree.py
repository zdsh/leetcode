"""
File: 897_Increasing_Order_Search_Tree.py
Date: 2019/02/18 17:10:13
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root.right != None:
            root_right = self.increasingBST(root.right)
            root.right = root_right

        if root.left != None:
            root_left = self.increasingBST(root.left)
            p = root_left
            while p.right != None:
                p = p.right
            p.right = root
            root.left = None
            root = root_left

        return root
            
            

