# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def travel(root, count):
            if root == None:
                return 0
            left = travel(root.left, count)
            right = travel(root.right, count)
            s = left + right + root.val
            if s not in count:
                count[s] = 0
            count[s] += 1
            return s
        count = {}
        travel(root, count)
        max_c = max(count.values())
        return [k for k in count if count[k] == max_c]        
