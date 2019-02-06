# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return ''

        if root.left == None and root.right == None:
            return chr(97 + root.val)

        if root.left != None:
            ret_left = self.smallestFromLeaf(root.left)
            if root.right == None:
                return ret_left + chr(97 + root.val)
        
        if root.right != None:
            ret_right = self.smallestFromLeaf(root.right)
            if root.left == None:
                return ret_right + chr(97 + root.val)
       
        if ret_left < ret_right:
             return ret_left + chr(97 + root.val)
        else:
             return ret_right + chr(97 + root.val)

        
