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
            if p.left != None:
                 root_list.append(p.left)
            else:
                if p.right != None:
                    return False
                while index < len(root_list):
                    p = root_list[index]
                    if p.left != None or p.right != None:
                        return False
                    index += 1
                return True

            if p.right != None:
                 root_list.append(p.right)
            else:
                while index < len(root_list):
                    p = root_list[index]
                    if p.left != None or p.right != None:
                        return False
                    index += 1
                return True
