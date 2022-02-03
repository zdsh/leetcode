# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getSum(root, height):
            if root.left == None and root.right == None:
                return height, root.val
            left_height, right_height = 0, 0
            if root.left:
                left_height, left_val = getSum(root.left, height+1)
            if root.right:
                right_height, right_val = getSum(root.right, height+1)

            if left_height > right_height:
                return left_height, left_val
            elif left_height < right_height:
                return right_height, right_val
            else:
                return left_height, left_val + right_val
       
        height, val = getSum(root, 0)
        return val
        
