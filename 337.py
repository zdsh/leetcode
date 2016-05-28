class Solution(object):
        
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return root.val
        else:
            self.rob(root.left)
            self.rob(root.right)
            a=0
            b=0
            if root.left!=None:
                a+=root.left.val
                if root.left.left!=None:
                    b+=root.left.left.val
                if root.left.right!=None:
                    b+=root.left.right.val
            if root.right!=None:
                a+=root.right.val
                if root.right.left!=None:
                    b+=root.right.left.val
                if root.right.right!=None:
                    b+=root.right.right.val
            root.val=max(b+root.val,a)
            return root.val
