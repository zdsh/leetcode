Solution for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def travel(self,root):
        if root==None:
            return
        self.travel(root.left)
        if self.pre!=None and self.first==None and self.pre.val>root.val:
            self.first=self.pre
        if self.first!=None and self.pre.val>root.val:
            self.second=root
        self.pre=root
        self.travel(root.right)
        
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root==None:
            return None
        self.first=None
        self.second=None
        self.pre=None
        self.travel(root)
        self.first.val,self.second.val=self.second.val,self.first.val
