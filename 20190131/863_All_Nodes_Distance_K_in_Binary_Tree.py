"""
File: 863_All_Nodes_Distance_K_in_Binary_Tree.py
Date: 2019/02/22 18:52:37
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        stack, q, step = [], root, 0
        def dfs(root, target, step):
            if root == target:
                return [(target, step)]
            ret = [(root, step)]
            if root.left:
                dfs_left = dfs(root.left, target, step + 1)
                if len(dfs_left) > 0:
                    return ret + dfs_left
            if root.right:
                dfs_right = dfs(root.right, target, step + 1)
                if len(dfs_right) > 0:
                    return ret + dfs_right
            return []

        ancestors = dfs(root, target, 0)
        ret = []
        def bfs(root, n):
            ret = []
            if n == 0:
                return [root.val]
            if root.left:
                ret += bfs(root.left, n - 1)
            if root.right:
                ret += bfs(root.right, n - 1)
            return ret

        for i in xrange(len(ancestors)):
             node, step = ancestors[i]
             if ancestors[-1][1] - step == K:
                 ret += [node.val]
                 continue
             if ancestors[-1][1] - step < K:
                 if i == len(ancestors) - 1:
                     ret += bfs(node, K)
                 else:
                     if node.left and node.left != ancestors[i+1][0]:
                         ret += bfs(node.left, K - 1 - ancestors[-1][1] + step)
                     if node.right and node.right != ancestors[i+1][0]:
                         ret += bfs(node.right, K - 1 - ancestors[-1][1] + step)
        return ret        
