# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getValue(root):
            if root == None:
                return 0, 0
            if root.left == None and root.right == None:
                return 0, root.val            
            s_left, val_left = getValue(root.left)
            s_right, val_right = getValue(root.right)
            return s_left + s_right + abs(val_right - val_left), val_left + val_right + root.val
        s, val = getValue(root)
        return s        
