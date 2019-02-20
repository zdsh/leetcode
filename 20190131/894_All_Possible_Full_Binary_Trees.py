"""
File: 894_All_Possible_Full_Binary_Trees.py
Date: 2019/02/20 20:34:01
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N % 2 == 0:
            return []
        if N == 1:
            root = TreeNode(0)
            return [root]
        if N == 3:
            root = TreeNode(0)
            root.left = TreeNode(0)
            root.right = TreeNode(0)
            return [root]

        ret = []
        for i in range(1, N - 1, 2):
            subrootlefts = self.allPossibleFBT(i)
            subrootrights = self.allPossibleFBT(N - 1 - i)
            for subrootleft in subrootlefts:
                for subrootright in subrootrights:
                    root = TreeNode(0)
                    root.left = subrootleft
                    root.right = subrootright
                    ret.append(root)
        return ret
             
