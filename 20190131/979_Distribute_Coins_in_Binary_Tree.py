# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        node_dic = {}
        node_dic[None] = [0, 0]
        def totolCoins(r):
            coins, node_num = 0, 0
            if r.left != None:
                ret_lef = totolCoins(r.left)
                coins += ret_lef[0]
                node_num += ret_lef[1]
            if r.right != None:
                ret_right = totolCoins(r.right)
                coins += ret_right[0]
                node_num += ret_right[1]
            node_dic[r] = [coins + r.val, node_num + 1]
            return node_dic[r]

        totolCoins(root)

        def minMoves(root, node_dic, coins_num_supply):
            ret = 0
            [coins_left, node_num_left] = node_dic[root.left]
            [coins_right, node_num_right] = node_dic[root.right]
            if root.left != None:
                ret += minMoves(root.left, node_dic, coins_left - node_num_left)
            if root.right != None:
                ret += minMoves(root.right, node_dic, coins_right - node_num_right)
            ret += abs(coins_right - node_num_right) + abs(coins_left - node_num_left)
            return ret
        ret = minMoves(root, node_dic, 0)
        return ret
