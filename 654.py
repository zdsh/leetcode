# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        max_num = max(nums)
        max_index = nums.index(max_num)
        if max_index == 0:
            left = None
        else:
            left = self.constructMaximumBinaryTree(nums[0:max_index])
        if max_index == len(nums) - 1:
            right = None
        else:
            right = self.constructMaximumBinaryTree(nums[max_index+1:])
        root = TreeNode(max_num, left, right)
        return root        
