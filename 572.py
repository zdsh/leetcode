# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        def check(root1, root2):
            if root1 == None and root2 == None:
                return True
            if root1 == None or root2 == None:
                return False
            if root1.val != root2.val:
                return False
            return check(root1.left, root2.left) and check(root1.right, root2.right)
     
        if root == None and subRoot == None:
            return True
        if root == None or subRoot == None:
            return False
        if root.val == subRoot.val:
            res = check(root, subRoot)
            if res:
                return True
        res = self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        if res:
            return True 
        return False
        
