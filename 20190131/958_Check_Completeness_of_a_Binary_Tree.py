"""
File: 958_Check_Completeness_of_a_Binary_Tree.py
Date: 2019/02/01 15:53:57
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        root_list = [root] 
        index = 0
        while index < len(root_list):       
            p = root_list[index]
            index += 1
            if p.left == None and p.right == None and index == len(root_list):
                return True
            if p.left != None:
                 root_list.append(p.left)
            if p.right != None:
                 root_list.append(p.right)
            if index == len(root_list):
                return True
            else:
                return False
        
