# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.values = {0:True}
        root.val = 0
        def travel(root, values):
            if root.left:
                root.left.val = 2 * root.val + 1
                values[root.left.val] = True
                travel(root.left, values)
            if root.right:
                root.right.val = 2 * root.val + 2
                values[root.right.val] = True
                travel(root.right, values)
            return root
        travel(root, self.values)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.values
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
