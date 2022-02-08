# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node
        if root == None:
            return root
        if depth == 2:
            node_left = TreeNode(val)
            node_right = TreeNode(val)
            node_left.left = root.left
            node_right.right = root.right
            root.left, root.right = node_left, node_right
            return root
        root.left = self.addOneRow(root.left, val, depth-1)
        root.right = self.addOneRow(root.right, val, depth-1)
        return root
