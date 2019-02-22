"""
File: 865_Smallest_Subtree_with_all_the_Deepest_Nodes.py
Date: 2019/02/22 20:38:01
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def get_depth(root):
            if root.left == None and root.right == None:
                return root, 1
            dleft, dright = 0, 0
            if root.left:
                subleft, dleft = get_depth(root.left)
            if root.right:
                subright, dright = get_depth(root.right)
            if dleft > dright:
                return subleft, dleft + 1
            if dright > dleft:
                return subright, dright + 1
            return root, dleft + 1

        return self.subtreeWithAllDeepest(root)[0]
