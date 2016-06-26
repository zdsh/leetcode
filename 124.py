#Solution for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        self.ret=root.val
        def solve(root):
            if root==None:
                return 0
            left=solve(root.left)
            self.ret=max(left+root.val,self.ret)
            right=solve(root.right)
            self.ret=max(right+root.val,self.ret)
            self.ret=max(left+right+root.val,self.ret)
            return max(max(left,right)+root.val,root.val)
        solve(root)
        return self.ret
        
